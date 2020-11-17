from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

#replace with your own colors and Raspimons
w = (255,255,255)
p = (128,0,128)
k = (0, 0, 0)


rest = [
        k, k, k, k, k, k, k, k,
        k, w, w, w, w, w, w, k,
        k, w, k, k, k, k, w, k,
        k, w, w, k, w, k, w, k,
        k, w, k, w, k, k, w, k,
        k, w, w, w, w, w, w, k,
        k, k, w, k, w, k, k, k,
        k, k, w, k, w, k, k, k
        ]
shake_left = [
        k, k, k, k, k, k, k, k,
        w, w, w, w, w, w, k, k,
        w, k, k, k, k, w, w, k,
        w, w, k, w, k, w, k, w,
        w, k, p, k, k, w, k, k,
        w, w, w, w, w, w, k, k,
        k, w, k, k, w, k, k, k,
        k, k, w, k, k, w, k, k
        ]

shake_right = [
        k, k, k, k, k, k, k, k,
        k, k, w, w, w, w, w, w,
        k, w, w, k, k, k, k, w,
        w, k, w, k, w, k, w, w,
        k, k, w, k, k, p, k, w,
        k, k, w, w, w, w, w, w,
        k, k, k, k, w, k, w, k,
        k, k, k, w, k, w, k, k
        ]

sense.set_pixels(shake_right) #set your own Raspimons here as default rest pose

#define your shake() function here:


    
#add your while True: loop below
        

        



