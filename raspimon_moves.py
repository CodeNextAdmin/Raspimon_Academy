
from pathlib import Path
import sys
p = Path().absolute() #get path to parent dir
sys.path.append(str(p.parent)) #append to module path
from raspimon_images import Raspimons
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
raspis = Raspimons() #create the instance so we can use the Raspimons as a raspis variable.

#now we can simply call on the raspis instance to get the one we want!
sense.set_pixels(raspis.get_open_mouth())
sleep(0.4)
sense.set_pixels(raspis.get_closed_mouth())
sleep(0.3)
sense.set_pixels(raspis.get_open_mouth())
sleep(0.4)
sense.set_pixels(raspis.get_closed_mouth())
sleep(0.3)
sense.set_pixels(raspis.get_open_mouth())
sleep(0.4)
sense.set_pixels(raspis.get_closed_mouth())
sleep(0.3)
sense.set_pixels(raspis.get_open_mouth())
sleep(0.4)
sense.set_pixels(raspis.get_closed_mouth())
sleep(0.3)

 

 

