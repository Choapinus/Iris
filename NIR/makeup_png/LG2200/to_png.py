import os
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=True, help="path to directory containing the dataset")
args = vars(ap.parse_args())
ls = [os.path.join(args['dir'], x) for x in os.listdir(args['dir'])]

for imdir in ls:
	# print(imdir)
	im = cv2.imread(imdir)
	os.remove(imdir)
	png = imdir.split('.')[0]+'.png'
	cv2.imwrite(png, im)

# print('done with {} images'.format(len(ls))