import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import colorsys
from PIL import Image

# (1) Import the file to be analyzed!
img_file = Image.open("colour test.png")
img = img_file.load()

# (2) Get image width & height in pixels
[xs, ys] = img_file.size
max_intensity = 100
hues = {}
rgb_list = []
rgb_freq = []
# (3) Examine each pixel in the image file
for x in range(0, xs):
  for y in range(0, ys):
    # (4)  Get the RGB color of the pixel
    [r, g, b] = img[x, y]
    found = False
    for k in range(len(rgb_list)):
        if rgb_list[k] == [r,g,b]:
            rgb_freq[k] += 1
            found = True
            print("found duplicate")
    if found == False:
        rgb_list.append([r,g,b])
        rgb_freq.append(1)

    # (5)  Normalize pixel color values
    r /= 255.0
    g /= 255.0
    b /= 255.0
for k in range(len(rgb_list)):
    print(rgb_list[k],rgb_freq[k])



img_file = Image.open("colour test.png")
img = img_file.load()

for x in range(0, xs):
  for y in range(0, ys):
    # (4)  Get the RGB color of the pixel
    [r, g, b] = img[x, y]
    found = False
    for k in range(len(rgb_list)):
        if rgb_list[k] == [r,g,b]:
            rgb_freq[k] += 1
            found = True
            print("found duplicate")
    if found == False:
        rgb_list.append([r,g,b])
        rgb_freq.append(1)

    # (5)  Normalize pixel color values
    r /= 255.0
    g /= 255.0
    b /= 255.0
for k in range(len(rgb_list)):
    print(rgb_list[k],rgb_freq[k])