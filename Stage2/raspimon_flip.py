from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (255,255,255)
p = (128,0,128)
k = (0, 0, 0)

raspimon1 = [
        k, k, k, k, k, k, k, k,
        k, w, w, w, w, w, w, k,
        k, w, k, k, k, k, w, k,
        k, w, w, k, w, k, w, k,
        k, w, k, p, k, k, w, k,
        k, w, w, w, w, w, w, k,
        k, k, w, k, w, k, k, k,
        k, k, w, k, w, k, k, k
        ]

raspimon2 = [
        k, k, k, k, k, k, k, k,
        k, p, p, p, p, p, k, k,
        k, p, k, k, k, k, p, k,
        k, p, w, k, w, k, p, k,
        k, p, k, w, k, k, p, k,
        k, p, p, p, p, p, p, k,
        k, k, p, k, p, k, k, k,
        k, k, p, k, p, k, k, k
    ]


 
sense.set_pixels(raspimon1)



while True:
    orientation = sense.get_orientation()
    sleep(.2)
    print(orientation)
       
    #declare a roll variable
    
    
    #write an if statement 

        
   
   
    
    

        
    

