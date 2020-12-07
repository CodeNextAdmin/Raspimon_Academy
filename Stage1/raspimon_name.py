from sense_emu import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep

#this is how you load the sense object so you can use it in this script.
sense = SenseHat()

#Two different views for the Raspimon, using RGB colors.
p = (128, 0, 128)
w = (255, 255, 255)
k = (0,0,0)

egg = [p,p,p,p,p,p,p,p,
       p,p,p,w,w,p,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,p,w,w,p,p,p,
       p,p,p,p,p,p,p,p]
       
hatched = [k,k,k,k,k,k,k,k,
           k,k,k,p,p,p,k,k,
           k,k,p,p,p,p,p,k,
           k,k,p,k,p,k,p,k,
           k,k,p,w,p,w,p,k,
           k,k,k,p,p,p,k,k,
           k,k,k,p,p,p,k,k,
           k,k,p,p,k,p,p,k ]
            


#add more messages below. 
sense.show_message("Hi, My name is Codey!" , text_colour=[255,0,0], back_colour=[ 0 ,0, 255], scroll_speed=0.05)

#the sense object has functions we can use: set_pixels. The value in the parentheses should be the egg.
sense.set_pixels(hatched)
