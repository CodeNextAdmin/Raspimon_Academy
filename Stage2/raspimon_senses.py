from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

k = (0, 0, 0) #blank
r = (255, 0, 0 ) #red
c = (0, 255, 255) #cyan
w = (255, 255, 255) #white


raspimon_hot = [
  k, k, k, k, k, k, k, k,
  k, r, r, r, r, r, r, k,
  k, r, k, k, k, k, r, k,
  k, r, r, k, r, k, r, k,
  k, r, k, k, k, k, r, k,
  k, r, r, r, r, r, r, k,
  k, k, r, k, r, k, k, k,
  k, k, r, k, r, k, k, k
]

raspimon_fine = [
  k, k, k, k, k, k, k, k,
  k, w, w, w, w, w, w, k,
  k, w, k, k, k, k, w, k,
  k, w, r, k, r, k, w, k,
  k, w, k, k, k, k, w, k,
  k, w, w, w, w, w, w, k,
  k, k, w, k, w, k, k, k,
  k, k, w, k, w, k, k, k
]

raspimon_cold = [
  k, k, k, k, k, k, k, k,
  k, c, c, c, c, c, c, k,
  k, c, k, k, k, k, c, k,
  k, c, r, k, r, k, c, k,
  k, c, k, k, k, k, c, k,
  k, c, c, c, c, c, c, k,
  k, k, c, k, c, k, k, k,
  k, k, c, k, c, k, k, k
]

sense.set_pixels(raspimon_fine)

#declare a temperature variable and assign it the value of sense.get_temperature()
temperature = sense.get_temperature()
temperature = int(temperature) #recast as an integer (whole number)
temperature = temperature * 9/5 + 32 # convert to Fahrenheit

humidity = sense.get_humidity()
humidity = int(temperature)

sense.show_message("Temp: " + str(temperature) + " F", scroll_speed=0.1)
sense.show_message("Hum: " + str(humidity) + " kPA" , scroll_speed=0.1)

sense.set_pixels(raspimon_fine)


#make a while True loop
while True:
   
    temperature = sense.get_temperature()
    temperature = int(temperature) #recast as an integer (whole number)
    temperature = temperature * 9/5 + 32 # convert to Fahrenheit

    humidity = sense.get_humidity()
    humidity = int(temperature)
    print("temp " + str(temperature))
    print("hum " + str(humidity))
    
    #Find the temperature threshold you can change
    if temperature > 102:
        sense.set_pixels(raspimon_hot)
    elif temperature <= 90:
        sense.set_pixels(raspimon_cold)
    else:
        sense.set_pixels(raspimon_fine)
    
    
