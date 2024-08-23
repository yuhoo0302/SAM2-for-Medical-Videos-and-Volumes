from sam2.build_sam import build_sam2_video_predictor

import numpy as np
import torch
import os
import cv2
import glob
import tqdm

torch.cuda.set_device(6) # set the GPU idx here

dataset_name = '...'
dataset_path = './{}/*'.format(dataset_name)

type_list = os.listdir(".../segmentations")

testing_frame_mode = 'max' # first, max
propagate_mode = 'bidirection' # forward2backward, bidirection, backward
prompt_mode = 'mask' # point, mask
point_num = 1 # for point prompt

saving_folder = 'testing_{}'.format(dataset_name)

print(type_list)


def find_all_indices(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

# load the model 
sam2_checkpoint = "./checkpoints/sam2_hiera_large.pt"
model_cfg = "sam2_hiera_l.yaml"
predictor = build_sam2_video_predictor(model_cfg, sam2_checkpoint)


for type_ in tqdm.tqdm(type_list, desc="All type"):
    # ensure test_type exists
    test_type = type_
    
    data_path = glob.glob(dataset_path+'/segmentations/{}'.format(test_type))

    num_type = 0
    print(saving_folder)
    for data_path_ in tqdm.tqdm(data_path, desc="Sub type"):
        
        video_dir = data_path_.replace(test_type, 'images').replace('/segmentations', '')

        frame_names = glob.glob(video_dir+'/*.png')
        frame_names.sort(key=lambda p: int(os.path.splitext(p)[0].split('/')[-1]))
        tmp_path = './{}/{}/{}'.format(saving_folder, type_, data_path_.split('/')[-3])
        tmp_path_png = glob.glob(tmp_path+'/*.png')
        tmp_path_num = len(tmp_path_png)

        mask_path = glob.glob(data_path_+'/*.png')
        mask_path.sort(key=lambda p: int(os.path.splitext(p)[0].split('/')[-1]))

        label_exist_list = []
        label_sum_list = []
        
        for m_ in mask_path:
            mask = cv2.imread(m_, 0)
            mask[mask!=0] = 1 
            label_sum_list.append(mask.sum())
            if mask.sum() > 10: # better set a threshold
                label_exist_list.append(1)
            else:
                label_exist_list.append(0)
        
        if np.sum(label_exist_list) == 0:
            continue
        # return the first frame index
        if testing_frame_mode == 'first':
            ann_idx = find_all_indices(label_exist_list, 1)[0]
        # return the frame index with the max label sum
        elif testing_frame_mode == 'max':
            ann_idx =np.argmax(label_sum_list)
            # for cutting the testing video clip
            first_idx = max(0, int(find_all_indices(label_exist_list, 1)[0]-np.sum(label_exist_list)*0.1))
            end_idx = min(len(label_exist_list), int(find_all_indices(label_exist_list, 1)[-1]+np.sum(label_exist_list)*0.1))
        
        with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16):
            # modify misc.py to remove tqdm
            inference_state = predictor.init_state(video_path=video_dir)
            predictor.reset_state(inference_state)
            ann_frame_idx = ann_idx
            ann_obj_id = 1

            mask = cv2.imread(mask_path[ann_idx], 0)
            mask[mask!=0] = 1 
            
            if prompt_mode == 'mask':
                # mask prompt
                _, out_obj_ids, out_mask_logits = predictor.add_new_mask(
                inference_state=inference_state,
                frame_idx=ann_frame_idx,
                obj_id=ann_obj_id,
                mask = mask
                )
            elif prompt_mode == 'point':
                points, labels = [], []
                assert len(points) != 0 or len(points) != 0, print("Please provide points and labels")
                points, labels = np.array([points]), np.array([labels]) # np.float32, np.int32
                _, out_obj_ids, out_mask_logits = predictor.add_new_points(
                    inference_state=inference_state,
                    frame_idx=ann_frame_idx,
                    obj_id=ann_obj_id,
                    points=points,
                    labels=labels,
                )
                
            
            # run propagation throughout the video and collect the results in a dict
            video_segments = {}  # video_segments contains the per-frame segmentation results
            # propagate_in_video: set reverse=True for reverse process; start_frame_idx: set the start frame index/none for annoatation
            # modify sam2_video_type.py to remove tqdm
            
            
            if propagate_mode == 'forward2backward':
                for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state, start_frame_idx=0):
                    video_segments[out_frame_idx] = {
                        out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
                        for i, out_obj_id in enumerate(out_obj_ids)
                    }
            
            elif propagate_mode == 'bidirection':
                # set max_frame_num_to_track to limit the number of frames to track
                for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state, max_frame_num_to_track=end_idx-ann_idx): # max_frame_num_to_track=end_idx-ann_idx
                    video_segments[out_frame_idx] = {
                        out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
                        for i, out_obj_id in enumerate(out_obj_ids)
                    }
                for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state, reverse=True, max_frame_num_to_track=ann_idx-first_idx): # max_frame_num_to_track=ann_idx-first_idx
                    video_segments[out_frame_idx] = {
                        out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
                        for i, out_obj_id in enumerate(out_obj_ids)
                    }
            
            elif propagate_mode == 'backward':
                for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
                    video_segments[out_frame_idx] = {
                        out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
                        for i, out_obj_id in enumerate(out_obj_ids)
                    }

            
            save_path = './{}/{}/{}'.format(saving_folder, test_type, data_path_.split('/')[-3])
            os.makedirs(save_path, exist_ok=True)   
            out_frame_idx_keys = video_segments.keys()

            
            # save the results
            for key_ in out_frame_idx_keys:
                for out_obj_id, out_mask in video_segments[key_].items():
                    out_frame_idx_ = str(key_).zfill(5)
                    cv2.imwrite(save_path+'/{}.png'.format(out_frame_idx_), out_mask[0]*255)
                    
    
            seg_idx = list(video_segments.keys())
            imgzeros = np.zeros((out_mask[0].shape[0],out_mask[0].shape[1]))
            for id_ in range(len(frame_names)):
                if id_ in seg_idx:
                    continue
                cv2.imwrite(save_path +'/{}.png'.format(str(id_).zfill(5)), imgzeros)
            
