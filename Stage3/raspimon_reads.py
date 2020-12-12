from sense_hat import SenseHat
from time import sleep
import vision_lib

#initialize your SenseHat instance below here
sense = SenseHat()

#paste your colors & Raspimon below here
r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen

basic = [
b, b, b, b, b, b, b, b,
b, r, r, r, r, r, r, b,
b, r, b, b, b, b, r, b,
b, r, r, b, r, b, r, b,
b, r, b, b, b, b, r, b,
b, r, r, r, r, r, r, b,
b, b, r, b, r, b, b, b,
b, b, r, b, r, b, b, b
]

basic2= [
k, k, k, k, k, k, k, k,
k, k, w, w, w, w, w, w,
k, w, w, k, k, k, k, w,
w, k, w, k, w, k, w, w,
k, k, w, k, k, p, k, w,
k, k, w, w, w, w, w, w,
k, k, k, k, w, k, w, k,
k, k, k, w, k, w, k, k
]

#Show your Raspimon on the LED matrix below here
sense.set_pixels(basic)

def see_writing(text):
    print(text)
    #your code below here
    sense.set_pixels(basic)
    sense.show_message('I read...')
    sleep(1)
    sense.show_message(text)
    greetings = ["What's good", 'Hi', 'Good Morning'], 
    if text in greetings:
        sense.show_message('Hello')
    sleep(1)
    sense.set_pixels(basic2)


if __name__ == '__main__':
    vision_lib.start_camera()
