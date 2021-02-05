from sense_hat import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep 
from signal import pause

sense = SenseHat()

#declare variables
g = (0, 255, 0)
r = (255, 0, 0)
w = (255, 255, 255)
k = (0, 0, 0)

open_mouth=[
  w, w, w, w, w, w, w, w,
  w, r, r, w, r, r, w, w,
  w, r, r, w, r, r, w, w,
  w, w, w, w, w, w, w, w,  
  w, k, k, k, k, k, w, w,
  w, k, r, r, r, k, w, w,
  w, k, r, r, r, k, w, w,
  w, w, w, w, w, w, w, w
    
]

closed_mouth=[
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
  w, r, r, w, r, r, w, w,
  w, r, r, w, r, r, w, w,  
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w,
  k, k, k, w, w, k, k, k
    
]


#set initial position for raspberry and raspimon




#define functions, go_up(), go_down(), go_left() and go_right()






#define a while loop
