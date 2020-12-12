from sense_hat import SenseHat
from time import sleep
import vision_lib

#initialize your SenseHat instance below here
sense = SenseHat()

#paste your colors & Raspimon below here
r = [139, 0, 0]
mon_w = [255, 255, 255]
mon_y = [250, 214, 29]
mon_oj = [225, 151, 32]
mon_br = [129, 30, 9]
mon_r = [246, 45, 20]
mon_b = [0, 0, 0]
mon_p = [255,105,180]
sky_b = [135,206,235]
grass_g = [0,154,23]

#Raspimon Idle
pimon_idle = [
    sky_b, mon_b, mon_b, sky_b, sky_b, sky_b, sky_b, mon_b,
    sky_b, sky_b, mon_y, mon_oj, sky_b, sky_b, sky_b, mon_oj,
    sky_b, sky_b, sky_b, mon_y, mon_y, mon_y, mon_y, mon_oj,
    mon_oj, mon_oj, sky_b, mon_y, mon_b, mon_y, mon_y, mon_b,
    mon_oj, mon_oj, sky_b, mon_r, mon_y, mon_y, mon_y, mon_oj,
    sky_b, mon_br, sky_b, mon_y, mon_oj, mon_oj, mon_oj, sky_b,
    grass_g, mon_br, mon_y, mon_oj, mon_y, mon_oj, mon_y, grass_g,
    grass_g, grass_g, mon_y, mon_oj, mon_br, mon_br, mon_oj, grass_g
]
        
#Raspimon happy face
pimon_happy = [
    mon_p, mon_b, mon_p, mon_p, mon_p, mon_p, mon_b, mon_p,
    mon_p, mon_y, mon_p, mon_p, mon_p, mon_p, mon_y, mon_p,
    mon_p, mon_y, mon_y, mon_y, mon_y, mon_y, mon_y, mon_p,
    mon_p, mon_y, mon_w, mon_b, mon_y, mon_w, mon_b, mon_p,
    mon_p, mon_y, mon_b, mon_b, mon_y, mon_b, mon_b, mon_p,
    mon_p, mon_r, mon_y, mon_y, mon_y, mon_y, mon_r, mon_p,
    mon_p, mon_y, mon_b, mon_y, mon_y, mon_b, mon_y, mon_p,
    mon_p, mon_y, mon_y, mon_b, mon_b, mon_y, mon_y, mon_p,
]

#Raspimon angry face
pimon_angry = [
    r, mon_b, r, r, r, r, mon_b, r,
    r, mon_y, r, r, r, r, mon_y, r,
    r, mon_y, mon_y, mon_y, mon_y, mon_y, mon_y, r,
    r, mon_y, mon_w, mon_b, mon_y, mon_w, mon_b, r,
    r, mon_y, mon_b, mon_b, mon_y, mon_b, mon_b, r,
    r, mon_r, mon_y, mon_y, mon_y, mon_y, mon_r, r,
    r, mon_y, mon_y, mon_b, mon_b, mon_y, mon_y, r,
    r, mon_y, mon_b, mon_y, mon_y, mon_b, mon_y, r
]

#Show your Raspimon on the LED matrix below here
sense.set_pixels(pimon_idle)

def see_emotion(emotion):
    print(emotion)
    #your code here
    if emotion == 'happy':
        sense.set_pixels(pimon_happy)
        sleep(5)
        sense.set_pixels(pimon_idle)
    elif emotion == 'angry':
        sense.set_pixels(pimon_angry)
        sleep(5)
        sense.set_pixels(pimon_idle)
    else:
        sense.set_pixels(pimon_idle)


if __name__ == '__main__':
    vision_lib.start_camera()
