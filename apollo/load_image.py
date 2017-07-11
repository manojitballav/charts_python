# This python file will help in loading the images
from PIL import Image

# Getting the image name from the user
na_img = raw_input("Enter the name of the image: ")
# Reading the image
img = Image.open(na_img)
# Getting the size of the image
a,b = img.size
