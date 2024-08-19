# SAM2 for Medical Images

This project focuses on evaluating the SAM2 on medical images (videos/volumes), especially from the perspective of a real clinical annotation scene. In SAM2, the performance of target tracking depends on the accuracy of the segmentation of the initial frame. The initial frame can be prompted by `point` or `mask` (`box` is not open-source now). Therefore, to obtain stable tracking and annotation effects, the user should choose to manually label the mask outline of one frame instead of clicking several points. Therefore, we plan to explore the performance that SAM2 can achieve when the user labels the frame's mask with the largest area and gives the frame position where the target appears and ends. We believe this to some extent reflects the potential of SAM2 in the application of medical moving object annotation.


## TotalSegmentor-MR
#### Modality: `MRI`
#### Target: `adrenal_gland_left, adrenal_gland_right, aorta, autochthon_left, autochthon_right, brain, colon, duodenum, esophagus, femur_left, femur_right, fibula, gallbladder, gluteus_maximus_left, gluteus_maximus_right, gluteus_medius_left, gluteus_medius_right, gluteus_minimus_left, gluteus_minimus_right, heart, hip_left, hip_right, humerus_left, humerus_right, iliac_artery_left, iliac_artery_right, iliac_vena_left, iliac_vena_right, iliopsoas_left, iliopsoas_right, inferior_vena_cava, intervertebral_discs, kidney_left, kidney_right, liver, lung_left, lung_right, pancreas, portal_vein_and_splenic_vein, prostate, quadriceps_femoris_left, quadriceps_femoris_right, sacrum, sartorius_left, sartorius_right, small_bowel, spinal_cord, spleen, stomach, thigh_medial_compartment_left, thigh_medial_compartment_right, thigh_posterior_compartment_left, thigh_posterior_compartment_right, tibia, urinary_bladder, vertebrae`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_mr1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_mr2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_mr3.png) [[Link]](https://github.com/wasserth/TotalSegmentator)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/totalsegmentor-mr1.gif" height="200"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/totalsegmentor-mr2.gif" height="200"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/totalsegmentor-mr3.gif" height="200"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/totalsegmentor-mr4.gif" height="200">
</div>


## MSD-Heart
#### Modality: `MRI`
#### Target: `left atrium`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDheart1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDheart2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDheart3.png) [[Link]](http://medicaldecathlon.com/)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_heart_mr1.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_heart_mr2.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_heart_mr3.gif" height="150"> 
</div>


## Cross-Modality Domain Adaptation for Medical Image Segmentation 2021
#### Modality: `T1-MRI`
#### Target: `cochleas, tumours`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_crossMoDA1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_crossMoDA2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/rresults_crossMoDA3.png) [[Link]](https://crossmoda.grand-challenge.org/)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/crossmoda_1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/crossmoda_2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/crossmoda_3.gif" height="150">
</div>


## MSD-Prostate
#### Modality: `Multimodal MRI (T2, ADC)`
#### Target: `prostate central gland, peripheral zone`
[[Dice-T2]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate11.png) [[HD-T2]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate12.png) [[IoU-T2]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate13.png) [[Dice-ADC]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate21.png) [[HD-ADC]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate22.png) [[IoU-ADC]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate23.png) [[Link]](http://medicaldecathlon.com/)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_T2_1.gif" height="130"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_ADC_1.gif" height="130"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_T2_2.gif" height="130"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_ADC_2.gif" height="130"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_T2_3.gif" height="130"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_ADC_3.gif" height="130">
</div>


## Multi-Centre, Multi-Vendor & Multi-Disease Cardiac Image Segmentation Challenge
#### Modality: `CMR`
#### Target: `left ventricle, left ventricular myocardium, right ventricle`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MMS1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MMS2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MMS3.png) [[Link]](https://ieeexplore.ieee.org/document/9458279)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/mms_1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/mms_2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/mms_3.gif" height="150">
</div>


## TotalSegmentor-CT
#### Modality: `CT`
#### Target: `adrenal_gland_left, adrenal_gland_right, aorta, atrial_appendage_left, autochthon_left, autochthon_right, brachiocephalic_trunk, brachiocephalic_vein_left, brachiocephalic_vein_right, brain, clavicula_left, clavicula_right, colon, common_carotid_artery_left, common_carotid_artery_right, costal_cartilages, duodenum, esophagus, femur_left, femur_right, gallbladder, gluteus_maximus_left, gluteus_maximus_right, gluteus_medius_left, gluteus_medius_right, gluteus_minimus_left, gluteus_minimus_right, heart, hip_left, hip_right, humerus_left, humerus_right, iliac_artery_left, iliac_artery_right, iliac_vena_left, iliac_vena_right, iliopsoas_left, iliopsoas_right, inferior_vena_cava, kidney_cyst_left, kidney_cyst_right, kidney_left, kidney_right, liver, lung_lower_lobe_left, lung_lower_lobe_right, lung_middle_lobe_right, lung_upper_lobe_left, lung_upper_lobe_right, pancreas, portal_vein_and_splenic_vein, prostate, pulmonary_vein, rib_left_1, rib_left_10, rib_left_11, rib_left_12, rib_left_2, rib_left_3, rib_left_4, rib_left_5, rib_left_6, rib_left_7, rib_left_8, rib_left_9, rib_right_1, rib_right_10, rib_right_11, rib_right_12, rib_right_2, rib_right_3, rib_right_4, rib_right_5, rib_right_6, rib_right_7, rib_right_8, rib_right_9, sacrum, scapula_left, scapula_right, skull, small_bowel, spinal_cord, spleen, sternum, stomach, subclavian_artery_left, subclavian_artery_right, superior_vena_cava, thyroid_gland, trachea, urinary_bladder, vertebrae_c1, vertebrae_c2, vertebrae_c3, vertebrae_c4, vertebrae_c5, vertebrae_c6, vertebrae_c7, vertebrae_l1, vertebrae_l2, vertebrae_l3, vertebrae_l4, vertebrae_l5, vertebrae_s1, vertebrae_t1, vertebrae_t10, vertebrae_t11, vertebrae_t12, vertebrae_t2, vertebrae_t3, vertebrae_t4, vertebrae_t5, vertebrae_t6, vertebrae_t7, vertebrae_t8, vertebrae_t9`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_TotalsegmentorCT1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_TotalsegmentorCT2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_TotalsegmentorCT4.png) [[Link]](https://github.com/wasserth/TotalSegmentator)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/TotalsegmentorCT1.gif" height="140"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/TotalsegmentorCT2.gif" height="140"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/TotalsegmentorCT3.gif" height="140"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/TotalsegmentorCT4.gif" height="140"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/TotalsegmentorCT5.gif" height="140"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/TotalsegmentorCT6.gif" height="140">
</div>



## MSD-Lung
#### Modality: `CT`
#### Target: `tumours`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDLung1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDLung2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDLung3.png) [[Link]](http://medicaldecathlon.com/)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_lung_1.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_lung_2.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_lung_3.gif" height="150"> 
</div>


## Multi-Atlas Labeling Beyond the Cranial Vault
#### Modality: `CT`
#### Target: `aorta, esophagus, gallbladder, inferior vena cava, left adrenal gland, left kidney, liver, pancreas, portal vein and splenic vein, right adrenal gland, right kidney, spleen, stomach`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MALBCV1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MALBCV2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MALBCV3.png) [[Link]](https://www.synapse.org/Synapse:syn3193805/wiki/217789)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/MALBCV_CT1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/MALBCV_CT2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/MALBCV_CT3.gif" height="150">
</div>


## STS-3D 2023
#### Modality: `CBCT`
#### Target: `teeth`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CBCT1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CBCT2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CBCT3.png) [[Link]](https://tianchi.aliyun.com/competition/entrance/532087)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct1.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct2.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct3.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct4.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct5.gif" height="150">
</div>



## ToothFairy2: Multi-Structure Segmentation in CBCT Volumes
#### Modality: `CBCT`
#### Target: `bridge, crown, implant, left inferior alveolar canal, left maxillary sinus, lower jawbone, lower left canine, lower left central incisor, lower left first molar, lower left first premolar, lower left lateral incisor, lower left second molar, lower left second premolar, lower left third molar (wisdom tooth), lower right canine, lower right central incisor, lower right first molar, lower right first premolar, lower right lateral incisor, lower right second molar, lower right second premolar, lower right third molar (wisdom tooth), pharynx, right inferior alveolar canal, right maxillary sinus, upper jawbone, upper left canine, upper left central incisor, upper left first molar, upper left first premolar, upper left lateral incisor, upper left second molar, upper left second premolar, upper left third molar (wisdom tooth), upper right canine, upper right central incisor, upper right first molar, upper right first premolar, upper right lateral incisor, upper right second molar, upper right second premolar, upper right third molar (wisdom tooth)`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_ToothFairy21.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_ToothFairy22.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_ToothFairy23.png) [[Link]](https://toothfairy2.grand-challenge.org/)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/ToothFairy_1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/ToothFairy_2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/ToothFairy_3.gif" height="150">
</div>



## EPFL_EM
#### Modality: `Electron Microscopy`
#### Target: `mitochondria`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_EM1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_EM2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_EM3.png) [[Link]](https://www.kaggle.com/datasets/kmader/electron-microscopy-3d-segmentation)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/mitochondria_em1.gif" height="200"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/mitochondria_em2.gif" height="200">
</div>

## ssTEM
#### Modality: `Electron Microscopy`
#### Target: `NeuralStructures`
[[Link]](https://imagej.net/events/isbi-2012-segmentation-challenge)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/NeuralStructures1.gif" height="200"> 
</div>


## CAMUS 
#### Modality: `Ultrasound`
#### Target: `left ventricle endocardium, left ventricle epicardium, left atrium`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CAMUS1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CAMUS2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CAMUS3.png) [[Link]](https://www.creatis.insa-lyon.fr/Challenge/camus/index.html)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/camus-us1.gif" height="200"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/camus-us2.gif" height="200">
</div>


## CardiacUDC 
#### Modality: `Ultrasound`
#### Target: `left ventricle (LV), right ventricle (RV), left atrium (LA), right atrium (RA)`
[[Link]](https://www.kaggle.com/datasets/xiaoweixumedicalai/cardiacudc-dataset)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/cardiacUDC_1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/cardiacUDC_2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/cardiacUDC-3.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/cardiacUDC-4.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/cardiacUDC-5.gif" height="150">
</div>


## EchoCP 
#### Modality: `Ultrasound`
#### Target: `left ventricle (LV), right ventricle (RV), left atrium (LA), right atrium (RA)`
[[Link]](https://www.kaggle.com/datasets/xiaoweixumedicalai/echocp)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/EchoCP-1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/EchoCP-2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/EchoCP-3.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/EchoCP-4.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/EchoCP-5.gif" height="150">
</div>


## CholecSeg8K
#### Modality: `Colonoscopy`
#### Target: `abdominal wall, blood, connective tissue, cystic duct, fat, gallbladder, gastrointestinal tract, grasper, hepatic vein, l-hook electrocautery, liver`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CholecSeg8K1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CholecSeg8K2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CholecSeg8K3.png) [[Link]](https://www.kaggle.com/datasets/newslab/cholecseg8k)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/CholecSeg8K-1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/CholecSeg8K-2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/CholecSeg8K-3.gif" height="150">
</div>


## SunSeg
#### Modality: `Colonoscopy`
#### Target: `PolyP`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_sunseg1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_sunseg2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_sunseg3.png) [[Link1]](http://amed8k.sundatabase.org/) [[Link2]](https://github.com/GewelsJI/VPS/blob/main/docs/DATA_PREPARATION.md)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sunseg1.gif" height="120"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sunseg2.gif" height="120"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sunseg3.gif" height="120"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sunseg4.gif" height="120"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sunseg5.gif" height="120">
</div>



## OCTA-500
#### Modality: `OCTA`
#### Target: `3D FAZ`
[[Link]](https://ieee-dataport.org/open-access/octa-500)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/octa500-1.gif" height="300"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/octa500-2.gif" height="300"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/octa500-3.gif" height="300">
</div>


## OCTA-500
#### Modality: `OCT`
#### Target: `choroid, intraretinal cysts, macular hole, retina`
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_OIMHSdatasets1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_OIMHSdatasets2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_OIMHSdatasets3.png) [[Link]](https://springernature.figshare.com/articles/dataset/OIMHS_dataset/23508453?backTo=%2Fcollections%2FOIMHS_An_Optical_Coherence_Tomography_Image_Dataset_Based_on_Macular_Hole_Manual_Segmentation%2F6662624&file=42522673)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/OIMHSdatasets-1.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/OIMHSdatasets-2.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/OIMHSdatasets-3.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/OIMHSdatasets-4.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/OIMHSdatasets-5.gif" height="150">
</div>






