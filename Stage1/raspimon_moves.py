from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

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

open_eyes = [
k, k, d, d, d, d, k, k,
k, d, d, w, d, w, d, k,
d, d, d, k, d, k, d, d,
d, d, r, d, d, d, r, d,
p, p, d, d, k, d, d, p,
k, r, r, d, d, d, p, k,
r, r, r, r, p, p, p, p,
k, k, k, k, k, k, k, k 
]       

closed_eyes =[
k, k, d, d, d, d, k, k,
k, d, d, d, d, d, d, k,
d, d, d, d, d, d, d, d,
d, d, r, d, d, d, r, d,
p, p, d, d, k, d, d, p,
k, r, r, d, d, d, p, k,
r, r, r, r, p, p, p, p,
k, k, k, k, k, k, k, k 
]

sense.set_pixels(open_eyes)

#Create animation below





print('Done')

