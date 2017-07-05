# This program contains the OOP model to detect luminance from an image

# importing the requried library files
from PIL import Image
import colorsys
import math


# importing the libraries for workbook
# from openpyxl import Workbook
# from openpyxl import load_workbook

# # Setting up the workbook
# wb = Workbook()
# ws = wb.create_sheet('Sheet',0)
# wb.save('S6.xlsx')

# # Declaring global variables
# r = 1
# c = 1

values = []
# Getting the image name from the user
na_img = raw_input("Enter the name of the image: ")
# Reading the image
img = Image.open(na_img)
# Getting the size of the image
a,b = img.size

# function to get relative brightness
def brightness(na_img):
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

# function to get the perceived brightness as per CIE 1931 XYZ color space
# def per_bright(na_img):
# 	sperb = 0
# 	# Traversing through all the pixels
# 	for x in range(1,a):
# 		for y in range(1,b):
# 			# Getting the RGB values of each pixels
# 			R,G,B = img.getpixel((x,y))
# 			perb = (0.2126*R)+(0.7152*G)+(0.0722*B)/3
# 			wb1 = load_workbook("S6.xlsx")
# 			ws = wb1.get_sheet_by_name('Sheet')
# 			ws.cell(row = x, column = y).value = perb
# 			sperb += perb
# 			wb1.save("data.xlsx")
# 			print "Done: "+str(x)+"x"+str(y)
# 	print "The average perceived luminance is: "+ str(sperb/(a*b))



# function to get the hsv value of each pixel
def hsv_color(na_img):
	for x in range(0,a):
		for y in range(0,b):
			# Getting the RGB values of each pixels
			R,G,B = img.getpixel((x,y))
			print colorsys.rgb_to_hsv(R,G,B)

# This is the reloaded function for solving data saving issues
# function to get the perceived brightness as per CIE 1931 XYZ color space
def per_bright(na_img):
	sperb = 0
	# Traversing through all the pixels
	for x in range(1,a):
		for y in range(1,b):
			# Getting the RGB values of each pixels
			R,G,B = img.getpixel((x,y))
			perb = (0.2126*R)+(0.7152*G)+(0.0722*B)/3
			sperb += perb
			values.append(perb) 
			# print "Done: "+str(x)+"x"+str(y)
	print "The average perceived luminance is: "+ str(sperb/(a*b))


# function to get the hsv value of each pixel
def hsl_color(na_img):
	H = 0.00
	L = 0.00
	S = 0.00
	for x in range(0,a):
		for y in range(0,b):
			# Getting the RGB values of each pixels
			R,G,B = img.getpixel((x,y))
			h,l,s = colorsys.rgb_to_hls(R,G,B)
			H += h
			L += l
			S += s
	print "The average hue is: "+str(float(H/(a*b)))
	print "The average saturation is: "+str(float(S/(a*b)))
	print "The average luminosity is: "+str(float(L/(a*b)))

# Function to calculate hue of each pixel
def hue_cal(na_img):
	fr,fg,fb = 0.00,0.00,0.00
	r,g,bx = 0.00,0.00,0.00
	for x in range(0,a):
		for y in range(0,b):
			# Getting the RGB values of each pixel
			R,G,B = img.getpixel((x,y))
			r = float(R/255)
			if r>fr:
				fr = r
			g = float(G/255)
			if g > fg:
				fg = g
			bx = float(B/255)
			if bx > fb:
				fb = bx
	print "The max value of RED is:"+str(fr)
	print "The max value of GREEN is:"+str(fg)
	print "The max value of BLUE is:"+str(fb)

def conversion(na_img):
	h = 0.00
	for x in range(0,a):
		for y in range(0,b):
			r,g,be = img.getpixel((x,y))
			r /= 255
			g /= 255
			be /= 255
			mx = max(r,g,be)
			mn = min(r,g,be)
			if(mx == r):
				# If red is the dominating color
				try:
					h = (g-be)/(mx-mn)
				except Exception, ZeroDivisonError:
					h = 0
			elif(mx == g):
				# If green is the dominating color
				try:
					h = 2 + (be-r)/(mx-mn)
				except Exception, ZeroDivisonError:
					h = 0
			elif(mx == be):
				# If blue is the dominating color
				try:
					h = 4 + (r-g)/(mx-mn)
				except Exception, ZeroDivisonError:
					h = 0
			else:
				print "There is some error in this pixel at: "+str(x)+","+str(y)

			# Matching as the hsl color whel
			h = h * 60
			# Checking whether H is a positive value 
			if (h > 0):
				print math.floor(h)
			else:
				# If H is negative
				print math.floor(360-h)

# Main function
def main() :
	print "The resolution of the loaded image is: "+str(a)+"x"+str(b)
	# brightness(na_img)
	per_bright(na_img)
	# print "Done with the workbook"
	# hsv_color(na_img)
	# hsl_color(na_img)
	# hue_cal(na_img)
	# conversion(na_img)
	for item in values:
		print item
	return "End of process"

    
# Calling the main function
if __name__ == "__main__" :
    main()