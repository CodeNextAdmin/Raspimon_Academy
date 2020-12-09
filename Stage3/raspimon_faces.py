from sense_hat import SenseHat
from time import sleep
import vision_lib

#initialize your SenseHat instance below here
sense = SenseHat()

#paste your colors & Raspimon below here


#Show your Raspimon on the LED matrix below here



def see_emotion(emotion):
    print(emotion)
    #your code below here
    sense.show_message(emotion)


if __name__ == '__main__':
    vision_lib.start_camera()
