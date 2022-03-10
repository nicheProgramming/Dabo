from asyncio.windows_events import NULL

# Define the possible symbols on the wheel
symbolShapes = ["square", 
                "triangle", 
                "circle", 
                "swirl", 
                "quark", 
                "ds9", 
                "blackHole"]

class instantiateWheel:
    def buildWheel(self, position):
        # The inner wheel doesn't need to account for color, the others do
        if self.position == 0:
            # Store shape, then number of shapes
            self.wheel = [["square", 3],
                          ["swirl", 1],
                          ["circle", 1],
                          ["triangle", 3],
                          ["circle", 1],  
                          ["triangle", 1],
                          ["square", 2],
                          ["ds9", 1],
                          ["square", 1],
                          ["square", 3],
                          ["circle", 3],
                          ["square", 2],
                          ["blackHole", 1],
                          ["circle", 1],
                          ["square", 3],
                          ["triangle", 2],
                          ["triangle", 1],
                          ["blackHole", 1],
                          ["circle", 3],
                          ["square", 1],
                          ["ds9", 1],
                          ["triangle", 2],
                          ["blackHole", 1],
                          ["circle", 2],
                          ["triangle", 1],
                          ["circle", 3],
                          ["quark", 1],
                          ["triangle", 3],
                          ["circle", 2],
                          ["triangle", 2],
                          ["square", 1],
                          ["ds9", 1],
                          ["triangle", 3],
                          ["square", 2],
                          ["blackHole", 1],
                          ["circle", 2],

            ]
        elif self.position == 1:

        elif self.position == 2:




class gameSymbol(object):
    def __init__(self, shape, num, color):
        self.shape = shape
        self.num = num
        self.color = color

    # shape = NULL
    # numOfShapes = 0
    # color = NULL
    # position = 0
    # wheel = 0

class result(object):
    def __init__(self, symOut, symMid, symIn):
        self.symOut = symOut
        self.symMid = symMid
        self.symIn = symIn

    def resultList(self):
        result = [self.symOut, self.symMid, self.symIn]
        return result

class slots:
    # Usable slots range from 32 to 4 in the bottom third, 8-16 in the right third, and 20-28 in the left third
    bettableSlotList = [None] * 27
    bet = 100

class payouts:
    def __init__(self, results):
        # Should be a 1x3 to 3x3 array, three symbols per slot, UP to three slots bet on
        self.results = results

