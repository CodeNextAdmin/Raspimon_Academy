from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Galbert" , "Freedy", "Voltria" , "Kat-Kat"]

names.append("Lizardia")

sense.show_message(names[1])

#Colors:
r = (255, 0, 0) # red to max value, no green or blue
w = (255, 255, 255) #white is all colors maxed
k = (0, 0, 0) #RGB black, but for LED it means off

#define another color. Use one letter variable names to make it easy later
g = (0, 255, 0)
l = (128, 255, 128) #lightGreen
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange

raspimon = [
k, k, k, k, k, k, k, k,
k, r, r, r, r, r, r, k,
k, r, k, k, k, k, r, k,
k, r, r, k, r, k, r, k,
k, r, k, k, k, k, r, k,
k, r, r, r, r, r, r, k,
k, k, r, k, r, k, k, k,
k, k, r, k, r, k, k, k
]
 
sense.set_pixels(raspimon)

#add a one-pixel mouth
sense.set_pixel(3,4, [255,0,0])
 
sleep(1.5)
sense.show_message("changing form...")

chirp1 = [k, k, k, k, k, k, k, k,
          k, k, k, l, r, y, k, k,
          k, k, k, l, l, k, k, k,
          l, g, g, w, w, g, g, l,
          k, l, g, w, w, l, g, k,
          k, k, l, w, w, l, k, k,
          k, k, k, l, l, k, k, k,
          k, k, o, k, k, o, k, k]

   
sense.set_pixels(chirp1)

