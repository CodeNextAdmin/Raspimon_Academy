"""change import statment to run on emulator """
from sense_hat import SenseHat
#from sense_emu import SenseHat
from time import sleep

sense = SenseHat()
sense.low_light = True

SHAKE_VAL = 2.4 # adjust sensitivity of shaking to save the current image.
YAW_TO_CLEAR = 300 # adjust to match your threshold for yaw (tilt left and right)

colors = []

#make a list to hold our current image, size 64 (0-63)
current_image = list(range(64)) 

#booleans to handle changign states
setting_color = False
moving = False
shaking = False
changing_color = False

#for accelerometer to detect shaking
x_accel = 0
y_accel = 0
z_accel = 0

sense.clear()

#define some colors as tuples with RGB values
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0, 0, 255)
lime = (0, 255, 0)
green = (0,160, 0)
yellow = (255,255,0)
orange = (255,165,0)
cyan = (0,255,255)
purple = (128,0,128)
pink = (255,20,147)
fuschia = (255,0,255)
navy = (0,0,128)
turquoise = (64,224,208)
chartreuse = (127,255,0)
gold = (255,215,0)
coral = (255,127,80)
brown = (165,42,42)
maroon = (165,42,42)
khaki = (240,230,140)
lavender = (230,230,250)

#load desired colors
colors.extend([white, red, gold ,blue, orange, purple, green, brown, cyan, black])

#welcome message


sense.show_message("Raspimon Builder." , text_colour=coral, back_colour=chartreuse, scroll_speed=.09)


#      canvas by changing all 64 values in our current_image to black.
for i in current_image:
    current_image[i] = black

#variables to store our current position and color
x = 0
y = 0
color = colors[0]

#start with a pixel in the top left corner
sense.set_pixel(x,y, color) 

#returns a white screen
def flash():
    global white
    W = white
    flash = [
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
        W,W,W,W,W,W,W,W,
    ]
    return flash

#clears all the pixels to black
def clear():
    global current_image
    B = black
    clear=[
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
        B,B,B,B,B,B,B,B,
    ]
    sense.set_pixels(clear)
    current_image = clear

#save the current image to file, also print it to console.
def save_image():
    global shaking 
    with open("LED_designs.txt", 'a+') as f:
        current_image = sense.get_pixels()
        f.write(str(current_image) + "\n")

    sense.set_pixels(flash()) #flash white to confirm saving.
    sleep(.3)
    sense.set_pixels(current_image)
    print("Saved: " + str(current_image))
    shaking = False


def next_color():

    global colors, color, changing_color
    changing_color = True
    #get the index of current color
    curr_index = colors.index(color)
   
    curr_index = curr_index + 1
    if curr_index >= len(colors):
        curr_index = 0

    color = colors[curr_index]
    print("new color set")
    

def set_all_pixels(color):
    leds = list(range(64))

    for i in leds:
        leds[i] = color

    sense.set_pixels(leds)


def show_colors():
    global colors

    for c in colors:
        set_all_pixels(c)
        sleep(.25)

    clear()
    sense.set_pixel(x,y,color)

def detect_shake():
    global x_accel, y_accel, z_accel, shaking

    #get the raw values for all 3 planes.
    acceleration= sense.get_accelerometer_raw()
    x_accel = acceleration["x"]
    y_accel = acceleration["y"]
    z_accel = acceleration["z"]

    #change negative values to positive with absolute value
    x_accel = abs(x_accel)
    y_accel = abs(y_accel)
    z_accel = abs(z_accel)

    #add all the values together.
    sum_shake = x_accel + y_accel + z_accel
   
   #if shaking meets our threshold, then save the image to file
    if sum_shake > SHAKE_VAL:
        shaking = True
        save_image()

def detect_orientation():
    global changing_color, setting_color
    orientation = sense.get_orientation_degrees()

    if orientation["yaw"] >= YAW_TO_CLEAR:
        flash()
        clear()


#main loop detecting changes to joystick and movement
while True:

    detect_shake()

    if shaking == False:
        detect_orientation()

    for event in sense.stick.get_events():
       
        moving = True

        if event.action == "pressed" and event.direction == "down":

            if y < 7 and y >= 0:
                   
                y = y + 1
                sense.set_pixels(current_image)             

        if event.action == "pressed" and event.direction == "up":
            
            if  y > 0:
                 
                y = y - 1
                sense.set_pixels(current_image)
                
                   
        if event.action == "pressed" and event.direction == "right":
    
            if x < 7 and x >=0:         
                x = x + 1          
                sense.set_pixels(current_image)
             
        if event.action == "pressed" and event.direction == "left":

            if x >= 0 and x <=7:
                 
                x = x - 1
                sense.set_pixels(current_image)
                        

        if event.action == "pressed"  and event.direction == "middle":

            sense.set_pixel(x,y,color)
            setting_color = True

            #convert coordinates to list index 
            current_pixel_index = (y*8) + x
            
            current_image[current_pixel_index] = color
            sense.set_pixels(current_image)


        if event.action == "held" and event.direction == "middle" and changing_color == False:
            
            next_color()
            


        if event.action == "released":
            moving = False
            setting_color = False
            changing_color = False


    if setting_color == False:
        sense.set_pixel(x,y,black)
        sleep(.2)
        sense.set_pixel(x,y,color)
        sleep(.2)












