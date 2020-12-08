import cv2
import numpy as np
from sense_hat import SenseHat

sense = SenseHat()
sense.clear() 


#colors
r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0)   #blank (black)
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen

colors = [r, g, b, k, w, c, y, o, n, p, d, l]
color_names = ['r', 'g', 'b', 'k', 'w', 'c', 'y', 'o', 'n', 'p', 'd', 'l']
# This maps all the colors to the names of the colors, so we can print them.
colors_to_names = dict(zip(colors, color_names))

# Put the location of your image file here.
IMG_FILE = '/home/pi/Downloads/voltorb.png'
# Set MATCH_COLORS to True to match the closest predefined color, otherwise we print the original value.
MATCH_COLORS = True

# This function just determines the absolute value distance between two colors a and b.
def distance(a, b):
    # for each r,g, and b, find the absolute distance, then sum those distances.
    return sum([abs(x - y) for x, y in zip(a, b)])


# Here we read the image file and make sure it is read appropriately.
img = cv2.imread(IMG_FILE)
if img is None:
    print('Error, invalid image file')
    exit

# Let's downsample the image to 8x8
resized = cv2.resize(img, (8, 8), interpolation=cv2.INTER_LANCZOS4)
# cv2 uses BGR instead of RGB like the sense hat, so lets convert that.
resized = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
# Now let's reshape it for the sense hat to be a list of 64 RGB pixels.
resized = np.reshape(resized, (64, 3))

if MATCH_COLORS:
    # final output will hold the colors for the final representation.
    final_output = []
    printed_output = []
    # let's go through and check each color from the resized image.
    for v in resized:
        # We will initialize the closest color as r and the distance as a very large number.
        closest_color = r
        dist = 1000000
        # Now we will go through and check the distance from the color in the resized image to the list of available colors.
        for c in colors:
            # Get the distance from color c, and the current image pixel v.
            curr_dist = distance(v, c)
            # If the distance is smaller (closer), update the distance and the closest color value.
            if curr_dist < dist:
                dist = curr_dist
                closest_color = c
        # We've gone through all the colors for this pixel and found the closest match.
        # Let's add that to the end of our new list and add the color name to our printed list.
        final_output.append(closest_color)
        printed_output.append(colors_to_names[closest_color])
    
    # Finally, let's print a comma delimted list of our color names for use in other python files.
    print('[ ' + ','.join(printed_output) + ' ]')
else:
    final_output = resized
    print(final_output)
sense.set_pixels(final_output)
