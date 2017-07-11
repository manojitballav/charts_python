from PIL import Image
import colorsys

svep = 0
# Traversing through all the pixels
for x in range(0,a):
	for y in range(0,b):
		# Getting the RGB values of each pixels
		R,G,B = img.getpixel((x,y))
		# Getting the brightness of each pixel
		avep = (R + G + B)/3
		svep += avep
# Getting the average brightness
print "The average luminance of the image is: "+ str(svep/(a*b))