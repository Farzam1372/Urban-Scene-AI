# Urban-Scene-AI
Using vision language models to understand urban driving scenes
✅ Project Explanation
Your project, Urban-Scene-AI, uses Vision-Language Models (e.g., CLIP) to automatically identify and understand unusual or critical situations in urban driving scenes.

🎯 Aim
Enhance autonomous driving safety by automatically detecting and describing rare or complex urban scenes (e.g., accidents, roadworks, unexpected pedestrian behavior).

📌 Dataset to Use
nuScenes (urban driving with rich annotations, ideal for autonomous driving tasks)

Alternative: BDD100K (Berkeley DeepDrive – urban road scenarios)

# Prepare Datasets
Download BDD100K
Please first download the images and annotations from the official website. For more details about the dataset, please refer to the official documentation.

On the official download page, the required data and annotations for each task are:
Link : https://bair.berkeley.edu/blog/2018/05/30/bdd/

image tagging set:
images: 100K Images
annotations: Detection 2020 Labels
object detection set:
images: 100K Images
annotations: Detection 2020 Labels
pose estimation set:
images: 100K Images
annotations: Pose Estimation Labels
instance segmentation set:
images: 10K Images
annotations: Instance Segmentation
semantic segmentation set:
images: 10K Images
annotations: Semantic Segmentation
panoptic segmentation set:
images: 10K Images
annotations: Panoptic Segmentation
drivable area set:
images: 100K Images
annotations: Drivable Area
box tracking (MOT) set:
images: MOT 2020 Images
annotations: MOT 2020 Labels
segmentation tracking (MOTS) set:
images: MOTS 2020 Images
annotations: MOTS 2020 Labels

We list all the tasks here for completeness, but you only need to download the images and labels for the task you are interested in.