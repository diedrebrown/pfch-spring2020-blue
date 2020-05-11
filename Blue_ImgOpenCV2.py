# Blue at the Rijksmuseum - Eval blue with OpenCV
# This code is based on the tutorial, Introduction to Deep Learning with OpenCV, by Jonathan Fernandes.


import numpy as np
import pandas as pd
import cv2
import csv

#import images
MeissenerblueMacaw = "MeissenerblueMacaw.jpg"
VerspronckportGirLDressed = 'VerspronckportGirLDressed.jpg'
VermeerWomanLet = 'VermeerWomanLet.jpg'
VermeerMilkmaid = 'VermeerMilkmaid.jpg'
deHoochDelousing = 'deHoochDelousing.jpg'
SintJansHolyKin = 'SintJansHolyKin.jpg'
BlueWashOntwerp = 'BlueWashOntwerp.jpg'
MeissnerblueParrot = 'MeissnerblueParrot.jpg'

bluerijksimgs = [MeissenerblueMacaw, VerspronckportGirLDressed, VermeerWomanLet, VermeerMilkmaid, deHoochDelousing, SintJansHolyKin, BlueWashOntwerp, MeissnerblueParrot]

with open('blueimgvals.csv', mode='w') as imgvals:
	imgwriter = csv.writer(imgvals, delimiter=',')
	header = ['imgName','imgSizeBGR','BlueVal','GreenVal','RedVal']
	imgwriter.writerow(header)
	imgcounter = 0
	for img in bluerijksimgs:
		# import image file into cv2
		imgfile = cv2.imread(bluerijksimgs[imgcounter]) 
		# confirm shape of image to confirm that image has been read
		print(imgfile.shape) # prints the rows, columns, and number of bgr channels of an image
		# for values closer to 0 = none of that color in image
		# for values closer to 255 = lots of that color in image
		blue = imgfile[:,:,0]
		green = imgfile[:,:,1]
		red = imgfile[:,:,2]
		print("Blue " + str(blue) + " Green " + str(green) + " Red: " + str(red))
		imgwriter.writerow([bluerijksimgs[imgcounter], imgfile.shape, blue, green, red])
		imgcounter += 1
		# # show image and image channels
		# # greyscale channel images will appear for blue, green, and red, respectively. 
		# # the closer to white/lighter an area is the more of that channel is in the image
		# cv2.imshow('Blue',blue)
		# cv2.imshow('Green',green)
		# cv2.imshow('Red',red)
		# cv2.imshow('Image',imgfile)
		# cv2.waitKey(3000)
		# cv2.destroyAllWindows()
	


