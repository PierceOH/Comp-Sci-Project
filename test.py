import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
from PIL import Image
output_mat = []
rgb_list = []
rgb_freq = []
colour_list = ["colour test.png","colour test2.png","colour test3.png","colour test5.png","colour test6.png","roof.png"]
lookup_list = []
for k in range(256):
    lookup_list.append([])


for k in range(len(colour_list)):
    # (1) Import the file to be analyzed!
    img_file = Image.open(colour_list[k])
    img = img_file.load()

    # (2) Get image width & height in pixels
    [xs, ys] = img_file.size
    max_intensity = 100
    hues = {}

    # (3) Examine each pixel in the image file
    for x in range(0, xs):
      for y in range(0, ys):
        # (4)  Get the RGB color of the pixel
        try:
            [r, g, b] = img[x, y]
        except ValueError:
            [r,g,b,_] = img[x,y]
            print("ERROR",x,y)


        found = False
        if colour_list[k] == "roof.png":
            print("roof")
            for rgb_val in range(len(lookup_list[r])):
                if [r,g,b] == lookup_list[r][rgb_val]:
                    lookup_list[r][rgb_val] = [0,0,0]
        else:
            for pixel in range(len(lookup_list[r])):
                if lookup_list[r][pixel] == [r,g,b]:
                    found = True
            if found == False:

                lookup_list[r].append([r,g,b])



        # (5)  Normalize pixel color values
        r /= 255.0
        g /= 255.0
        b /= 255.0

print("-----------------------INITILISATION COMPLETE-------------------------")

img_file = Image.open("test_map.png")
img = img_file.load()

    # (2) Get image width & height in pixels
[xs, ys] = img_file.size

max_intensity = 100
hues = {}

    # (3) Examine each pixel in the image file
pixel_count = 0
prev_perc = 0

for x in range(0, xs):
    output_mat.append([0])
    curr_perc = int((x/xs)*100)
    if prev_perc!= curr_perc:
        print(curr_perc,"%")
    prev_perc = curr_perc

    for y in range(0, ys):
        output_mat[x].append(0)
        # (4)  Get the RGB color of the pixel
        [r, g, b] = img[x, y]
        for k in range(len(lookup_list[r])):
            if lookup_list[r][k] == [r,g,b]:
                pixel_count += 1
                output_mat[x][y] = 1
        # (5)  Normalize pixel color values        r /= 255.0
        r /= 255.0
        g /= 255.0
        b /= 255.0


print(int((pixel_count/(xs*ys))*100),"% of the map is roads")
print(len(output_mat),len(output_mat[0]),xs,ys)

import numpy as np
import scipy.misc as smp

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros( (2048,2048,3), dtype=np.uint8 )

for k in range(len(output_mat)):
    for i in range(len(output_mat[k])):# Makes the middle pixel red
        if output_mat[k][i] == 1:
            data[i,k] = [0,0,255]   # Makes the next pixel blue
        else:
            data[i,k] = [255,255,255]
img = smp.toimage( data )       # Create a PIL image
img.show()