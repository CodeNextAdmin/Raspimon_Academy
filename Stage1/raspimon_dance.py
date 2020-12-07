from sense_hat import SenseHat
from time import sleep


sense = SenseHat()

r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan


#load the Raspimons you want to animate
klaw = [
c, w, w, c, w, w, c, c,
c, w, k, c, w, k, c, c,
c, r, c, c, r, c, c, c,
c, r, c, c, r, c, c, c,
r, r, r, r, r, c, r, r,
r, r, k, k, r, r, r, c,
r, r, r, r, r, c, r, r,
r, c, r, c, r, c, c, c
]

klaw3 = [
c, w, k, c, w, k, c, c,
c, w, w, c, w, w, c, c,
c, r, c, c, r, c, c, c,
c, r, c, c, r, c, c, c,
r, r, r, r, r, c, r, r,
r, r, r, r, r, r, r, c,
r, r, r, r, r, c, r, r,
r, c, r, c, r, c, c, c
]

klaw4 = [
c, w, k, c, w, k, c, c,
c, w, w, c, w, w, c, c,
c, r, c, c, r, c, c, c,
c, r, c, c, r, c, c, c,
r, r, r, r, r, c, r, r,
r, r, k, k, r, r, r, c,
r, r, r, r, r, c, r, r,
r, c, r, c, r, c, c, c
]

klaw5 = [
c, c, w, c, w, c, c, c,
c, c, k, c, k, c, c, c,
c, c, r, c, r, c, c, c,
c, c, r, c, r, c, c, c,
c, r, r, r, r, r, r, c,
c, r, k, k, r, r, r, c,
r, r, r, r, r, r, r, r,
r, c, r, c, r, c, r, c
]

klaw6 = [
c, c, w, c, w, c, c, c,
c, c, k, c, k, c, c, c,
c, c, r, c, r, c, c, c,
c, c, r, c, r, c, c, c,
c, r, r, r, r, r, r, c,
c, r, r, k, k, r, r, c,
r, r, r, r, r, r, r, r,
r, c, c, r, c, r, c, r
]


for i in range(20):
    sense.set_pixels(klaw)
    sleep(.3)
    sense.flip_h()
    sleep(.2)
    sense.flip_h()
    sleep(.1)
    sense.flip_h()
    sleep(.2)
    sense.flip_h()
    sleep(.1)
    sense.set_pixels(klaw3)
    sleep(.3)
    sense.set_pixels(klaw4)
    sleep(.1)
    sense.set_pixels(klaw3)
    sleep(.3)
    sense.set_pixels(klaw4)
    

  
while True:
    #dance forever!
    sense.set_pixels(klaw5)
    sleep(.2)
    sense.set_pixels(klaw6)
    sleep(.3)
