from sense_hat import SenseHat
from time import sleep
#import pynput
from pynput  import keyboard

sense = SenseHat()


# colors
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)
     

#sample Raspimons
rmon1 = [k, k, k, l, r, y, k, k,
         k, k, k, l, l, k, k, k,
         k, k, g, w, w, g, k, k,
         k, k, g, w, w, g, k, k,
         k, k, l, w, w, l, k, k,
         k, k, l, w, w, l, k, k,
         k, k, k, l, l, k, k, k,
         p, p, o, p, p, o, p, p ]

rmon2 = [k, k, k, l, r, y, k, k,
         k, k, k, l, l, k, k, k,
         k, k, g, w, w, g, k, k,
         k, g, g, w, w, g, g, k,
         l, l, k, w, w, k, g, l,
         k, k, k, l, l, k, k, k,
         k, k, o, k, k, o, k, k,
         k, k, k, k, k, k, k, k ]      
           

rmon3 = [k, k, k, k, k, k, k, k,
        k, k, k, l, r, y, k, k,
        k, k, k, l, l, k, k, k,
        l, g, g, w, w, g, g, l,
        k, l, g, w, w, l, g, k,
        k, k, l, w, w, l, k, k,
        k, k, k, l, l, k, k, k,
        k, k, o, k, k, o, k, k ]         


rmon4 = [k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         o, l, g, g, g, g, l, r,
         k, k, g, l, l, g, k, y,
         k, k, k, k, l, l, k, k,
         k, k, k, k, l, l, k, k,
         k, k, k, k, k, l, k, k,
         k, k, k, k, k, k, k, k ]     
              


rmon5 = [k, k, k, l, l, k, k, k,
         k, k, k, l, g, g, k, k,
         k, k, k, k, g, g, k, k,
         o, l, g, l, l, g, l, r,
         k, k, k, w, w, w, k, y,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k,
         k, k, k, k, k, k, k, k ]      
        


rmon6 = [k, k, k, l, r, y, k, k,
         k, k, k, l, l, k, k, k,
         k, k, g, w, w, g, k, k,
         k, k, g, w, w, g, g, k,
         k, k, l, w, w, l, l, l,
         k, k, l, w, w, k, k, k,
         k, k, k, l, l, k, k, k,
         p, p, o, p, p, o, p, p ]      
        
        
sense.set_pixels(rmon1)        
 
#declare a current_action variable 
current_action = "rest"

         
#add your on_press() function
def on_press(key):
    global current_action
    letter = str(key)
    #sense.show_letter(key)
    #sense.show_letter(letter[1])
    if letter[1] == 'h':
        print("hovering...")
        current_action = "hover"
    elif letter[1] == 'f':
        print("flying...")
        current_action = "fly"
    elif letter[1] == 's':
        print("shuffling...")
        current_action = "shuffle"
    else:
        current_action = "rest"


#add your listener
listener = keyboard.Listener(on_press=on_press)
listener.start()


#add a while loop
while True:
    if current_action == 'hover':
        sense.set_pixels(rmon2)
        sleep(.2)
        sense.set_pixels(rmon3)
        sleep(.3)

    elif current_action == 'shuffle':
        sense.set_pixels(rmon6)
        sense.flip_h()
        sleep(.3)
        sense.flip_h()
        sleep(.3)

    elif current_action == 'fly':
        sense.set_pixels(rmon4)
        sleep(.3)
        sense.set_pixels(rmon5)
        sleep(.3)
    else:
        sense.set_pixels(rmon1)
        
        
