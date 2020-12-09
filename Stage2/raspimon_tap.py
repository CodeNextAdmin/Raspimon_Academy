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
while True:
    accel = sense.get_accelerometer_raw()
    sense.set_pixels(rest) #replace with your own

    x = accel["x"] #get each separate float value
    y = accel["y"]
    z = accel["z"]
    
    #changes all negative values to positive
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    #round to 3 dec. values
    x = round(x, 3)  
    y = round(x, 3)
    
    #the sum simplifies the detection of taps.  
    sum = x+y
    print(str(sum))
     
    #the value will need to be tested. When you get a value that works, add it below.   
    if sum > .1:
        print("Tap")
        sense.set_pixels(tapped)
        sleep(.5)
         
        

 
