from sense_hat import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep 

sense = SenseHat()
sense.clear()

g = (0, 255, 0)
r = (255, 0, 0)
w = (255, 255, 255)
k = (0, 0, 0)


open_mouth=[
  w, w, w, w, w, w, w, w,
  w, r, r, w, r, r, w, w,
  w, r, r, w, r, r, w, w,
  w, w, w, w, w, w, w, w,  
  w, k, k, k, k, k, w, w,
  w, k, r, r, r, k, w, w,
  w, k, r, r, r, k, w, w,
  w, w, w, w, w, w, w, w
    
]

closed_mouth=[
  k, k, k, k, k, k, k, k,
  w, w, w, w, w, w, w, w,
  w, r, r, w, r, r, w, w,
  w, r, r, w, r, r, w, w,  
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w,
  k, k, k, w, w, k, k, k
    
]



#sense.set_pixels(backyard)

#declare a variable to hold the current x, y location:
raspimon_x = 1
raspimon_y = 1
sense.set_pixel(raspimon_x, raspimon_y, w)

food_x = 6
food_y = 7

sense.set_pixel(food_x, food_y, r)

is_hungry = True


def go_up():
  global raspimon_y
  if raspimon_y >= 1:
    raspimon_y = raspimon_y - 1
    update()
    
    
def go_down():
  global raspimon_y
  if raspimon_y < 7:
    raspimon_y = raspimon_y + 1
    update()
   
  
def go_left():
  global raspimon_x
  if raspimon_x >= 1:
    raspimon_x = raspimon_x - 1
    update()
  
def go_right():
  global raspimon_x
  if raspimon_x < 7:
    raspimon_x = raspimon_x + 1
    update()
 

def update():
  global raspimon_x, raspimon_y
  sense.clear()
  sense.set_pixel(raspimon_x, raspimon_y, w)
  sense.set_pixel(food_x, food_y, r)
  print("updated...")
  
def eat():
  for i in range(10):
    sense.set_pixels(closed_mouth)
    sleep(.3)
    sense.set_pixels(open_mouth)
    sleep(.2)
    
  is_hungry = False
    


while is_hungry:
  
  for event in sense.stick.get_events():
    print(event)

    if event.direction == "down" and event.action == "released":
      print("Down")
      go_down()
      
    if event.direction == "up" and event.action == "released":
      print("Up")
      go_up()
      
    if event.direction == "right" and event.action == "released":
      print("Right")
      go_right()

    if event.direction == "left" and event.action == "released":
      print("Left")
      go_left()
      
      
    if raspimon_x == food_x and raspimon_y == food_y:
      print("Chomp chomp chomp")
      eat()
      
