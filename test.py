import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
from PIL import Image
rgb_list = []
rgb_freq = []
colour_list = ["colour test.png","colour test2.png","colour test3.png","colour test4.png"]
lookup_list = []
for k in range(256):
    lookup_list.append([])
print(lookup_list[255])

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
        [r, g, b] = img[x, y]

        found = False

        for k in range(len(lookup_list[r])):
            if lookup_list[r][k] == [r,g,b]:
                found = True
                print("found duplicate")
        if found == False:
            print("appending")
            lookup_list[r].append([r,g,b])
            print(lookup_list[r])


        # (5)  Normalize pixel color values
        r /= 255.0
        g /= 255.0
        b /= 255.0

print("-----------------------INITILISATION COMPLETE-------------------------")
print(lookup_list[146])
print(lookup_list[1],lookup_list[85])