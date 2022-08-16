# Iris Datasets

Andres Valenzuela and Juan Tapia

## paper 01

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis eget ex fringilla, feugiat tortor porta, congue purus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris dapibus turpis id venenatis porttitor. Mauris ornare, magna vel tempus bibendum, est neque congue tortor, vel rhoncus dolor est nec ante. Donec tempus, ante interdum vehicula mollis, velit elit consectetur eros, sit amet mollis erat metus semper ipsum. Aliquam a pretium sem. Nunc nec neque auctor nibh egestas finibus ut non sapien. Sed sed nunc sem. Nunc consequat quam sed elit faucibus, sed suscipit est bibendum. Duis ultrices lobortis fermentum.

## paper 02

Vivamus vitae tortor pharetra, tempus justo non, pellentesque dolor. Sed vel felis feugiat tortor suscipit elementum quis vel lorem. Aliquam erat volutpat. Proin libero augue, faucibus id massa sed, ultricies ornare eros. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce ut lectus et purus vehicula rhoncus. Proin semper odio sed volutpat lacinia. Morbi efficitur gravida odio, at vulputate dui sodales sed.


![figure_vis_vs_nir](https://github.com/Choapinus/Iris/blob/master/static/vis_vs_nir.png?raw=true)
<em>Example of images of each dataset. On the upper side we can found NIR images examples, and at the bottom side we can found VIS examples.</em>


## NIR Datasets

- OpenEDS: is a data set of eye images captured using a virtual-reality HMD with two synchronized eye-facing cameras at a frame rate of 200 Hz under controlled illumination.This dataset is composed of: Semantic segmentation data set collected with 152 participants of 12,759 images with annotations at a resolution of 400×640. Generative data set collected with 152 participants of 252,690 images at a resolution 400×600. Sequence data set collected with 152 participants of 91,200 images at a resolution of 400×640, with duration of 1.5 seconds for each participant, sampled at 200 Hz. Left and right paired human eye corneal topography in the form of point cloud collected for 143 participants. 

Dataset available from the source: https://www.v7labs.com/open-datasets/facebook-openeds


- [Alcohol-db](https://github.com/Choapinus/alcohol-db): 5 sessions of NIR image capturing were done for each person at intervals of 00, 15, 30, 45 and 60 minutes after having ingested alcohol.
Traditional databases available to test iris segmentation have not present images with iris captured under alcohol consumption on NIR or Visual Spectrum. This database was captured using two different iris NIR sensors: Iritech Gemini, and Iritech Venus.

Dataset available from: insert link

- Makeup-db: Traditional datasets for testing iris segmentation do not include photos of iris acquired under cosmetic effects on the NIR or Visual Spectrum. This dataset provides 530 images from 48 subjects, where each ROI (iris, pupil, sclera) of the images were labeled with VIA v2.0.5.

Dataset available form: insert link




## VIS Datasets



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


## Information
- @Juan Tapia - juan.tapia-farias@h-da.de
- @Andres Valenzuela - andres.valenzuela@tocbiometrics.com


## Disclaimer
The datasets, the implementation, or trained models used is restricted to research purposes. Using the datasets or the implementation/trained models for product development or comercial product is not allowed.
