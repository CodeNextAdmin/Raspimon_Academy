from sense_hat import SenseHat
import time
import random


sense = SenseHat()


raspimon_egg =  [(128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128)]
raspimon_hatched = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [248, 20, 144], [248, 20, 144], [248, 20, 144], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [248, 20, 144], [248, 20, 144], [248, 20, 144], [248, 20, 144], [248, 20, 144], [0, 0, 0], [0, 0, 0], [0, 0, 0], [248, 20, 144], [248, 0, 0], [248, 20, 144], [248, 0, 0], [248, 20, 144], [0, 0, 0], [0, 0, 0], [0, 0, 0], [248, 20, 144], [248, 252, 248], [128, 0, 128], [248, 252, 248], [248, 20, 144], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [248, 20, 144], [248, 20, 144], [248, 20, 144], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [248, 20, 144], [0, 0, 0], [248, 20, 144], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [248, 20, 144], [248, 20, 144], [0, 0, 0], [248, 20, 144], [248, 20, 144], [0, 0, 0]]


saved_state_file = open("current_state.txt","r")


current_state = saved_state_file.readlines()[0]

print(current_state)
saved_state_file.close()


food = 0



fortunes = ["you will prosper", "you will meet someone new", "love is near"]

print(random.choice(fortunes))




def save_current_state():
    global current_state
    file = open("current_state.txt", "w")
    file.write(current_state) # will overwrite 
    file.close() #close the file.
    
    
    
    
    print("saving...")
    
    
        
def feed(amt):
    global food, current_state
    food = food + amt #incrase by the amount of shaking.     
    if food > 50:
        current_state = 'hatched'
        print("hatched")
        save_current_state()
         
    
    
    
    
while True:
    
    accel = sense.get_accelerometer_raw()  

    x = accel["x"] #get each separate float value
    y = accel["y"]
    z = accel["z"]
    
    x = abs(x)
    y = abs(y)
    z = abs(y)
       
    shaking = x+y+z
    
    print("currently " + current_state)
    
    if shaking > 3.5 and shaking < 6:
        feed(shaking) # pass in the amount of shaking
        
    if current_state == 'egg':
        sense.set_pixels(raspimon_egg)
    elif current_state == 'hatched':
        sense.set_pixels(raspimon_hatched)
        

        
        
        
        
    
        
        
        
        
        
        
        
                
        
        
        
        
        
        