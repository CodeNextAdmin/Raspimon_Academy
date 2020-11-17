from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

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
tapped = [
        k, k, k, k, k, k, k, k,
        k, p, p, p, p, p, p, k,
        k, p, k, k, k, k, p, k,
        k, p, p, k, p, k, p, k,
        k, p, k, p, k, k, p, k,
        k, p, p, p, p, p, p, k,
        k, k, p, k, p, k, k, k,
        k, k, p, k, p, k, k, k
        ]

sense.set_pixels(rest) #set your own Raspimons here as default rest pose

#add a while True: loop below
        


        

 