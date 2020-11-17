from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Galbert" , "Freedy", "Voltria" , "Kat-Kat"]

names.append("Lizardia")

sense.show_message(names[1])

#Colors:

r = (255, 0, 0 ) # RED color, stored in an another data structure called a tuple.
k = (0, 0, 0) # black means zero amounts of red, green and blue

#define another color. Use one letter variable names to make it easy later

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

 


