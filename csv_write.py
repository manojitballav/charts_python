import csv
cs = open('chicken.csv', 'wb')
cs_file = csv.writer(cs, delimiter="	")
for i in range(100):
	cs_file.writerow(["Chicken"])
cs.close()




import csv
cs  = open('S6.csv','wb')
cs_file = csv.writer(cs,delimiter=",")
def csv_bright(na_img):
	sperb = 0
	# Traversing through all the pixels
	for x in range(1,a):
		for y in range(1,b):
			# Getting the RGB values of each pixels
			R,G,B = img.getpixel((x,y))
			perb = (0.2126*R)+(0.7152*G)+(0.0722*B)/3
			cs_file.writerow([perb])
			sperb += perb
			values.append(perb)
			# print "Done: "+str(x)+"x"+str(y)
	print "The average perceived luminance is: "+ str(sperb/(a*b))
	cs.close()