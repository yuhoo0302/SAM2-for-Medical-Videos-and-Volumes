# SAM2 for Medical Images

This project focuses on evaluating the SAM2 on medical images (videos/volumes), especially from the perspective of a real clinical annotation scene. In SAM2, the performance of target tracking depends on the accuracy of the segmentation of the initial frame. The initial frame can be prompted by `point` or `mask` (`box` is not open-source now). Therefore, to obtain stable tracking and annotation effects, the user should choose to manually label the mask outline of one frame instead of clicking several points. Therefore, we plan to explore the performance that SAM2 can achieve when the user labels the frame's mask with the largest area and gives the frame position where the target appears and ends. We believe this to some extent reflects the potential of SAM2 in the application of medical moving object annotation.


## TotalSegmentor-MR
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_mr1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_mr2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_mr3.png) [[Link]](https://github.com/wasserth/TotalSegmentator)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/totalsegmentor-mr1.gif" height="200"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/totalsegmentor-mr2.gif" height="200"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/totalsegmentor-mr3.gif" height="200"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/totalsegmentor-mr4.gif" height="200">
</div>

## Electron Microscopy Dataset (mitochondria)
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_EM1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_EM2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_EM3.png) [[Link]](https://www.kaggle.com/datasets/kmader/electron-microscopy-3d-segmentation)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/mitochondria_em1.gif" height="200"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/mitochondria_em2.gif" height="200">
</div>


## CAMUS 
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CAMUS1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CAMUS2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CAMUS3.png) [[Link]](https://www.creatis.insa-lyon.fr/Challenge/camus/index.html)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/camus-us1.gif" height="200"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/camus-us2.gif" height="200">
</div>


## CholecSeg8K
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CholecSeg8K1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CholecSeg8K2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CholecSeg8K3.png) [[Link]](https://www.kaggle.com/datasets/newslab/cholecseg8k)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/CholecSeg8K-1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/CholecSeg8K-2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/CholecSeg8K-3.gif" height="150">
</div>

## STS-3D CBCT
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CBCT1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CBCT2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_CBCT3.png) [[Link]](https://tianchi.aliyun.com/competition/entrance/532087)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct1.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct2.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct3.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct4.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/sts_cbct5.gif" height="150">
</div>

## MSD-Heart
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDheart1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDheart2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDheart3.png) [[Link]](http://medicaldecathlon.com/)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_heart_mr1.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_heart_mr2.gif" height="150"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_heart_mr3.gif" height="150"> 
</div>

## MSD-Prostate (T2/ADC)
[[Dice-T2]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate11.png) [[HD-T2]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate12.png) [[IoU-T2]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate13.png) [[Dice-ADC]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate21.png) [[HD-ADC]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate22.png) [[IoU-ADC]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MSDprostate23.png) [[Link]](http://medicaldecathlon.com/)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_T2_1.gif" height="130"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_ADC_1.gif" height="130"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_T2_2.gif" height="130"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_ADC_2.gif" height="130"> <img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_T2_3.gif" height="130"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/msd_prostate_ADC_3.gif" height="130">
</div>


## Multi-Atlas Labeling Beyond the Cranial Vault-CT
[[Dice]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MALBCV1.png) [[HD]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MALBCV2.png) [[IoU]](https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_MALBCV3.png) [[Link]](https://www.synapse.org/Synapse:syn3193805/wiki/217789)
<div align="center">
<img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/MALBCV_CT1.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/MALBCV_CT2.gif" height="150"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/videos/MALBCV_CT3.gif" height="150">
</div>
