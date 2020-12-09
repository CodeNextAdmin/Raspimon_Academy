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
def shake():
    print("shaking")
    sense.set_pixels(shake_left)
    sleep(.2)
    sense.set_pixels(shake_right)
    sleep(.2)
    sense.set_pixels(shake_left)
    sleep(.2)
    sense.set_pixels(shake_right)
    sleep(.2)
    sense.set_pixels(shake_left)
    sleep(.2)
    sense.set_pixels(shake_right)

    
#add your while True: loop below
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
    z = round(z, 3)
    
    #print( "x : " + str(x) + " y : " + str(y) + " z : " +str(z))
    sum = x+y+z
    print(str(sum))
    
    if sum > 3: 
        print("shake")
        shake()


