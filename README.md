# SAM2 for Medical Images

This project focuses on evaluating the SAM2 on medical images (videos/volumes), especially from the perspective of a real clinical annotation scene. In SAM2, the performance of target tracking depends on the accuracy of the segmentation of the initial frame. The initial frame can be prompted by `point` or `mask` (`box` is not open-source now). Therefore, to obtain stable tracking and annotation effects, the user should choose to manually label the mask outline of one frame instead of clicking several points. Therefore, we plan to explore the performance that SAM2 can achieve when the user labels the frame's mask with the largest area and gives the frame position where the target appears and ends. We believe this to some extent reflects the potential of SAM2 in the application of medical moving object annotation.


 ## TotalSegmentor-MR
<div align="center"><img src="https://github.com/yuhoo0302/SAM2-for-Medical-Images/blob/main/results/results_mr1.png" width="50%"></div>
