from sense_hat import SenseHat
from time import sleep
from collections import Counter

sense = SenseHat()

#Raspimon colors
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

chirp = [o, y, y, y, y, y, y, o,
         o, o, n, y, y, n, o, o,
         y, k, w, y, y, k, w, y,
         y, k, k, y, y, k, k, y,
         y, y, y, k, k, y, y, y,
         n, n, n, y, y, n, n, n,
         n, n, n, y, y, n, n, n,
         n, n, n, y, y, n, n, n
]   

frankie=[o, k, k, k, k, k, k, o,
         o, g, g, g, g, g, g, o,
         o, l, l, l, l, l, l, o,
         l, g, k, g, g, k, g, l,
         l, g, g, g, g, g, g, l,
         o, g, k, k, k, k, g, o,
         o, l, g, g, g, g, l, o,
         o, o, g, g, g, g, o, o
]       
        
codey = [c, w, c, c, c, c, w, c,
         c, p, p, d, d, p, p, c,
         c, d, w, d, d, w, d, c,
         c, d, k, d, d, k, d, c,
         d, d, d, d, d, d, d, d,
         c, d, d, k, d, d, d, c,
         g, g, d, d, d, d, g, g,
         g, g, g, d, d, g, g, g
]       


raspee =[k, w, w, d, d, d, k, k,
         w, w, w, d, d, d, k, k,
         d, d, w, w, w, w, d, k,
         d, d, w, n, n, n, d, k,
         w, w, n, k, n, k, d, k,
         k, k, n, n, n, n, k, k,
         n, c, c, y, y, o, c, p,
         k, p, p, k, p, p, k, k
]

wubby = [k, k, d, d, d, d, k, k,
         k, d, d, w, d, w, d, k,
         d, d, d, k, d, k, d, d,
         d, d, r, d, d, d, r, d,
         p, p, d, d, k, d, d, p,
         k, r, r, d, d, d, p, k,
         r, r, r, r, p, p, p, p,
         k, k, k, k, k, k, k, k
]

sullie = [ w,o,w,w,w,w,o,w,w,c,c,c,c,c,c,w,w,c,c,c,c,c,c,w,c,c,k,w,w,k,c,w,c,b,c,k,k,c,b,c,c,c,c,c,c,c,c,w,w,w,c,c,c,c,w,w,w,b,c,w,w,c,b,w ]

volt = [ p,p,r,r,r,r,p,p,p,r,r,r,r,r,r,p,r,w,r,r,r,w,r,r,r,w,k,r,w,w,r,r,r,r,r,r,r,r,r,r,w,w,w,w,w,w,w,w,p,w,w,w,w,w,w,p,p,p,w,w,w,w,p,p ]

# This function will find the most common color from a raspimon
def most_common_color(raspimon):
    # let's get the occurences, a dictionary of color values paired with the number of times they show up.
    occurrences = Counter(raspimon)
    #print(occurrences)
    # Let's find the most common occurence that's not k (empty color)
    top_count = 0
    top_color = k
    for color, count in occurrences.items():
        if count > top_count and color != k:
            top_count = count
            top_color = color
    #print(top_color)
    return top_color


raspimons = [ raspee, chirp, frankie, codey, wubby, sullie, volt]
names = ['raspee', 'chirp', 'frankie', 'codey', 'wubby', 'sullie', 'volt']
while True:
    for name, raspimon in zip(names, raspimons):
        sense.show_message(name, text_colour=most_common_color(raspimon), scroll_speed=0.08)
        sense.set_pixels(raspimon)
        sleep(2)    
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        
