class Raspimons:
    def __init__(self):
        
        #Edit your color list here:
        r = (255, 0, 0 ) #Red 
        b = (0, 0, 0) #Black
        
        
        #basic Raspimons
        self.closed_mouth = [
            b, b, b, b, b, b, b, b,
            b, r, r, r, r, r, r, b,
            b, r, b, b, b, b, r, b,
            b, r, r, b, r, b, r, b,
            b, r, b, b, b, b, r, b,
            b, r, r, r, r, r, r, b,
            b, b, r, b, r, b, b, b,
            b, b, r, b, r, b, b, b
        ]
        
        self.open_mouth = [
            b, b, b, b, b, b, b, b,
            b, r, r, r, r, r, r, b,
            b, r, b, b, b, b, r, b,
            b, r, r, b, r, b, r, b,
            b, r, b, r, b, b, r, b,
            b, r, r, r, r, r, r, b,
            b, b, r, b, r, b, b, b,
            b, b, r, b, r, b, b, b
        ]

        self.closed_eyes = [
        b, b, b, b, b, b, b, b,
        b, r, r, r, r, r, r, b,
        b, r, b, b, b, b, r, b,
        b, r, b, b, b, b, r, b,
        b, r, b, r, b, b, r, b,
        b, r, r, r, r, r, r, b,
        b, b, r, b, r, b, b, b,
        b, b, r, b, r, b, b, b
       ]

    #functions below return the desired Raspimon defined as lists above
    #make sure to keep the same structure, and indentation if you add more.
    def get_open_mouth(self):

        return self.open_mouth

    def get_closed_mouth(self):

        return self.closed_mouth

    def get_closed_eyes(self):

        return self.closed_eyes