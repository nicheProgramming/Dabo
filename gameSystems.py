import random
import gameSettings

minBet = 100
maxBet = 1000000
startingCreditCount = maxBet

class gameSymbol(object):
    def __init__(self, shape, num, color = None):
        self.shape = shape
        self.num = num
        self.color = color
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

class wheel(object):
    def __init__(self, slots, bet):
        self.slots = slots
        self.bet = bet
        self.wheel = gameSettings.instantiateWheel.buildWholeWheel()
        self.wheelOffset = [0, 0, 0]
    
    def spinWheel(self):
        self.wheelOffset = [random.randRange(0, 35), random.randRange(0, 35), random.randRange(0, 35)]
