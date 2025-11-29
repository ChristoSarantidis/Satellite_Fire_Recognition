# Satellite_Fire_Recognition

![](https://github.com/user-attachments/assets/a271f829-7b7c-4a80-b27c-18530468068e) ![](https://github.com/user-attachments/assets/f372e4c4-fd02-4de6-b961-19a087b5d2d4) ![](https://github.com/user-attachments/assets/0c4bc269-4405-4399-b8d3-317b5ab41f53)





Greetings :DD!

This is a project about forest fire detection using satellites. For those results 5 fold cross validation was used. It is a comparative study of YOLOv9tiny, YOLOv10nano, YOLOv11nano and YOLOv12nano algorithms (Family of yolo algorithm, for reference check original YOLO Algorithm paper, available at: 
https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Redmon_You_Only_Look_CVPR_2016_paper.html). 

The experiments where conducted using the following preprocessing techniques without preprocessing, detection aware cropping, data augmentation, histogram equilization and the combination of those techniques. In detail:

1) Without preprocessing: Images where not processed at all before feeding into the neural network.
2) Detection aware cropping (Crop): After inference phase, cropping based on the output of the model was performed. If there was a low detection prediction (<=0.5), then this image would pass again through the model in order to examine whether the predicted detection was True Positive or False Positive. For more information about how cropping was performed you can also check this paper: https://www.mdpi.com/2624-6120/6/4/60, titled Smoke Detection on the Edge: A Comparative Study of YOLO Algorithm Variants.
3) Data augmentation (Augment): Data augmentation was applied to the images as they were fed into the neural network, suvh as random cropping, translate, random rotation etc
4) Histogram Equilization (HEQ): Heq was applied to all images before they were fed into the neural network.
5) Combination of Crop and Augment: After training amd testing the model with augmented data, Detection aware cropping was performed.
6) Combination of Crop and HEQ: After feeding the Histogram Equalized images into the model and testing it, Detection aware cropping was performed.
7) Combination of HEQ and Augment: After performing HEQ, HEQ images and augmented HEQ images were fed into the model.
8) Combination of Crop, HEQ and Augment: After performing HEQ, HEQ images and augmented HEQ images were fed into the model. In addition to, Crop was applied after the inference phase.

A total of 5 folds where used. Fold details:

-Total images: 500
-Train images: 360
-Validation images: 40
-Inference images: 100

Based on the results, we can observe the following:

  -> **Best performance:** For the YOLOv12 variant, the Without preprocessing configuration provides a solid balance between Precision, Recall, and F1-score, with an mAP50 of 0.531. The training time is also reasonable at 257.7 seconds, with a test time of 4.11 seconds, making it an efficient choice for the given task. This suggests that, even without any preprocessing, YOLOv12 demonstrates competitive performance in wildfire detection.

  -> **Worst performance:** The combination of Crop, HEQ, and Augment consistently leads to the lowest values across all metrics for YOLOv12, with an F1-score of 0.363 and mAP50 of 0.339. The combination of multiple preprocessing techniques appears to have a detrimental effect on model performance for this variant, potentially due to overfitting or mismatched data augmentation strategies.

  -> **Fold comparison:** The results for Fold 1 and Fold 2 suggest similar trends in performance, with Fold 1 generally yielding slightly higher metrics than Fold 2, particularly in the Without preprocessing and Crop-Augment configurations. Fold 1 appears to have provided a better validation set, leading to more robust results across preprocessing techniques.

In summary, YOLOv12 performed best with no preprocessing, while the combination of Crop, HEQ, and Augment resulted in significantly reduced performance. These insights could guide future experiments on preprocessing strategies and highlight the importance of careful hyperparameter tuning to avoid potential negative impacts on the detection algorithm's accuracy.

For more details about this experiment, you can contact me at: csarantidis@ionio.gr
I'll be delighted to provide you with any additional information!!! ;D

The original dataset was retrieved from Roboflow. Available at: https://universe.roboflow.com/htw-berlin-xv7eo/satellite-wildfire-detection

*********Important notice************
I used this dataset for training purposes and i still have not been able to verify its provenance. It is not published in any academic research that is publicly available.
