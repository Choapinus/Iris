# Iris Datasets

Andres Valenzuela and Juan Tapia

## Towards an Efficient Segmentation Algorithm for Near-Infrared Eyes Images.

Semantic segmentation has been widely used for several applications, including the detection of eye structures. This is used in tasks such as eye-tracking and gaze estimation, which are useful techniques for human-computer interfaces, salience detection, and Virtual reality (VR), amongst others. Most of the state of the art techniques achieve high accuracy but with a considerable number of parameters. This article explores alternatives to improve the efficiency of the state of the art method, namely DenseNet Tiramisu, when applied to NIR image segmentation. This task is not trivial; the reduction of block and layers also affects the number of feature maps. The growth rate (k) of the feature maps regulates how much new information each layer contributes to the global state, therefore the trade-off amongst grown rate (k), IOU, and the number of layers needs to be carefully studied. The main goal is to achieve a light-weight and efficient network with fewer parameters than traditional architectures in order to be used for mobile device applications. As a result, a DenseNet with only three blocks and ten layers is proposed (DenseNet10). Experiments show that this network achieved higher IOU rates when comparing with Encoder-Decoder, DensetNet56-67-103, MaskRCNN, and DeeplabV3+ models in the Facebook database. Furthermore, this method reached 8th place in The Facebook semantic segmentation challenge with 0.94293 mean IOU and 202.084 parameters with a final score of 0.97147. This score is only 0,001 lower than the first place in the competition. The sclera was identified as the more challenging structure to be segmented.

## Semantic Segmentation of Periocular Near-Infra-Red Eye Images Under Alcohol Effects

This paper proposes a new framework to detect, segment, and estimate the localization of the eyes from a periocular Near-Infra-Red iris image under alcohol consumption. This stage will take part in the final solution to measure the fitness for duty. Fitness systems allow us to determine whether a person is physically or psychologically able to perform their tasks. Our segmentation framework is based on an object detector trained from scratch to detect both eyes from a single image. Then, two efficient networks were used for semantic segmentation; a Criss-Cross attention network and DenseNet10, with only 122,514 and 210,732 parameters, respectively. These networks can find the pupil, iris, and sclera. In the end, the binary output eye mask is used for pupil and iris diameter estimation with high precision. Five state-of-the-art algorithms were used for this purpose. A mixed proposal reached the best results. A second contribution is establishing an alcohol behavior curve to detect the alcohol presence utilizing a stream of images captured from an iris instance. Also, a manually labeled database with more than 20k images was created. Our best method obtains a mean Intersection-over-Union of 94.54% with DenseNet10 with only 210,732 parameters and an error of only 1-pixel on average.

## Alcohol Consumption Detection from Periocular NIR Images Using Capsule Network

This work proposes a method to detect alcohol consumption from a Near-Infra-Red (NIR) periocular eye images. The study focuses on determining the effect of external factors such as alcohol on the Central Nervous System (CNS). The goal is to analyse how this impacts on iris and pupil movements and if it is possible to capture these changes with a standard iris NIR camera. This paper proposes a novel Fused Capsule Network (F-CapsNet) to classify iris NIR images taken under alcohol consumption subjects. The results show the F-CapsNet algorithm can detect alcohol consumption in iris NIR images with an accuracy of 92.3% using half of parameters than the standard Capsule Network algorithm. This work is a step forward for developing an automatic system to estimate "Fitness for Duty" and prevent accidents due to alcohol consumption.

## Selfie Periocular Verification Using an Efficient Super-Resolution Approach

In this work is proposed an Efficient Single Image Super-Resolution algorithm, which takes into account a trade-off between the efficiency and the size of its filters. To that end, the method implements a loss function based on the Sharpness metric used to evaluate iris images quality. The method drastically reduces the number of parameters compared to the state-of-the-art: from 2,170,142 to 28,654. Our best results on remote verification systems with no redimensioning reached an EER of 8.89% for FaceNet, 12.14% for VGGFace, and 12.81% for ArcFace. Then, embedding vectors were extracted from SR images, the FaceNet-based system yielded an EER of 8.92% for a resizing of x2, 8.85% for x3, and 9.32% for x4.

![figure_vis_vs_nir](https://github.com/Choapinus/Iris/blob/master/static/vis_vs_nir.png?raw=true)
<em>Example of images of each dataset. On the upper side we can found NIR images examples, and at the bottom side we can found VIS examples.</em>


## NIR Datasets

- OpenEDS: is a data set of eye images captured using a virtual-reality HMD with two synchronized eye-facing cameras at a frame rate of 200 Hz under controlled illumination.This dataset is composed of: Semantic segmentation data set collected with 152 participants of 12,759 images with annotations at a resolution of 400×640. Generative data set collected with 152 participants of 252,690 images at a resolution 400×600. Sequence data set collected with 152 participants of 91,200 images at a resolution of 400×640, with duration of 1.5 seconds for each participant, sampled at 200 Hz. Left and right paired human eye corneal topography in the form of point cloud collected for 143 participants. 

Dataset available from source: https://www.v7labs.com/open-datasets/facebook-openeds

<p align="center">
  <img src="https://github.com/Choapinus/Iris/blob/master/static/openeds_example.png?raw=true" width="200" height="320">
</p>


- [Alcohol-db](https://github.com/Choapinus/alcohol-db): 5 sessions of NIR image capturing were done for each person at intervals of 00, 15, 30, 45 and 60 minutes after having ingested alcohol.
Traditional databases available to test iris segmentation have not present images with iris captured under alcohol consumption on NIR or Visual Spectrum. This database was captured using two different iris NIR sensors: Iritech Gemini, and Iritech Venus.

Dataset available from: insert link

<p align="center">
  <img src="https://user-images.githubusercontent.com/45126159/172894528-9f4d44b9-4d2d-4c9c-9f71-66dce00940bb.png" width=400>
</p>

- Makeup-db: Traditional datasets for testing iris segmentation doesn't include photos of iris acquired under cosmetic effects on the NIR or Visual Spectrum. This dataset provides 530 images from 48 subjects, where each ROI (iris, pupil, sclera and makeup) of the images was labeled with VIA v2.0.5.

Dataset available form: insert link

<p align="center">
  <img src="https://github.com/Choapinus/Iris/blob/master/static/makeup_example.png?raw=true" width="400">
</p>




## VIS Datasets

- MobBIO: The MobBIO dataset comprises the biometric data from 152 volunteers by using an Asus EeePad Transformer tablet, with mobile biometric systems in mind. Each subject provided samples of face, iris, and voice, but for this repository only the iris images were stored. There are on average 8 images for each subject.


- NTNU/Nokia: The NTNU dataset comprises the biometric data from 152 volunteers and 3,139 total images. Each subject provided samples of left and right iris and there are in average 11 images for each subject from a NOKIA N93i mobile.


## Citation:
```
@ARTICLE{9200989,
  author={Valenzuela, Andres and Arellano, Claudia and Tapia, Juan E.},
  journal={IEEE Access}, 
  title={Towards an Efficient Segmentation Algorithm for Near-Infrared Eyes Images}, 
  year={2020},
  volume={8},
  number={},
  pages={171598-171607},
  doi={10.1109/ACCESS.2020.3025195}}
```
```
@ARTICLE{9502109,
  author={Tapia, Juan E. and Droguett, Enrique Lopez and Valenzuela, Andres and Benalcazar, Daniel P. and Causa, Leonardo and Busch, Christoph},
  journal={IEEE Access}, 
  title={Semantic Segmentation of Periocular Near-Infra-Red Eye Images Under Alcohol Effects}, 
  year={2021},
  volume={9},
  number={},
  pages={109732-109744},
  doi={10.1109/ACCESS.2021.3101256}}
```
```
@capsule_cite{}
```
```
@article{tapia2022selfie,
  title={Selfie Periocular Verification Using an Efficient Super-Resolution Approach},
  author={Tapia, Juan E and Valenzuela, Andres and Lara, Rodrigo and Gomez-Barrero, Marta and Busch, Christoph},
  journal={IEEE Access},
  volume={10},
  pages={67573--67589},
  year={2022},
  publisher={IEEE}
}
```


## Information
- @Juan Tapia - juan.tapia-farias@h-da.de
- @Andres Valenzuela - andres.valenzuela@tocbiometrics.com


## Disclaimer
The datasets, the implementation, or trained models used is restricted to research purposes. Using the datasets or the implementation/trained models for product development or comercial product is not allowed.
