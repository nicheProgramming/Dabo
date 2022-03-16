import random
import gameSettings

minBet = 100
maxBet = 1000000
startingCreditCount = maxBet

def placeBet(slotsBetOn):
    # Store [slot bet on, amount bet on slot] x 3 
    placedBets = [[], [], []]
    index = 0

    while slotsBetOn > 0:
        print("Which slot would you like to bet on?")
        slot = input()

        print("How much would you like to bet on slot " + str(slot) + "?")
        bet = input()

        # Make sure bet is in acceptable range
        if bet < minBet:
            print ("Bet too small, try again.")
        elif bet > maxBet:
            print ("bet too large, try agian.")
        else:
            placedBets[index] = [slot, bet]

        index += 1
        slotsBetOn -= 1 
    return placedBets

class gameSymbol(object):
    def __init__(self, shape, num, color = None):
        self.shape = shape
        self.num = num
        self.color = color
        # position = 0
        # wheel = 0

class result(object):
    def __init__(self, wheel, bets):
        # array of all three wheel positions AFTER spin
        self.wheel = wheel
        # 3 x 2 array of [slot, bet], 0 being inner wheel. We only care about slot
        self.bets = bets

    def resultList(self):
        # result must store a 3 x 3 array containing ALL THREE results per slot
        result = [0, 0, 0]

        # for [slot, bet] in self.bets
        # thus, bet = [slot, bet]
        for index, bet in enumerate(self.bets):
            if bet != []:
                # set result at index to [inSym, midSym, outSym]
                result[index][0] = self.wheel[0][(bet[0])]
                result[index][1] = self.wheel[1][(bet[0])]
                result[index][2] = self.wheel[2][(bet[0])]
            else:
                # if bet is empty, return empty results
                result[index] = []

        return result

class slots:
    # Usable slots range from 32 to 4 in the bottom third, 8-16 in the right third, and 20-28 in the left third
    bettableSlotList = [None] * 27
    bet = 100

class payouts:
    def __init__(self, bets, results):
        # Should be a 1x3 to 3x3 array, three symbols per slot, UP to three slots bet on
        self.bets = bets
        self.results = results
    
    def calculatePayouts(self):
        payouts = [0, 0, 0]

        # result iterations through results (each loop assesses a single ring's result array)
        # resultInArray = [shape, numOfShape]
        # resultMidAndOut = [shape, numOfShape, color]
        for index, result in enumerate(self.results):
            # If two shapes match
            if result[0][0] == result[1][0] OR result[1][0] == result[2][0] OR result[0][0] = result[2][0]:
                # if two counts match
                if result[0][1] == result[1][1] OR result[1][1] == result[2][1] OR result[0][1] = result[2][1]:
                    payouts[index] = 0

                #RESUME WORK HERE, YOU NEED TO EVALUATE LARGER MATCHES BEFORE SMALLER ONES
        return payouts


class wheel(object):
    def __init__(self):
        self.wheel = gameSettings.instantiateWheel.buildWholeWheel()
        self.wheelOffset = [0, 0, 0]
        # Debug variables
        self.referenceWheel = gameSettings.instantiateWheel.buildWholeWheel()
    
    def spinWheel(self):
        self.wheelOffset = [random.randRange(0, 35), random.randRange(0, 35), random.randRange(0, 35)]

        for index, spin in enumerate(self.wheelOffset[0]):
            self.wheel[0] = self.wheel[0][1:] + self.wheel[0][0]
            print("First item in self.wheel[2] is " + str(self.wheel[0][0]))
            # Print the expected wheel item to ensure array is moving as anticipated
            print ("expected: " + self.referenceWheel[0][(-1-index)])

        for index, spin in enumerate(self.wheelOffset[1]):
            # This is reversed on purpose, this wheel spings counter clockwise unlike the other two 
            self.wheel[0] = self.wheel[1][-1] + self.wheel[2][:-1]
            print("First item in self.wheel[1] is " + str(self.wheel[1][0]))
            # Print the expected wheel item to ensure array is moving as anticipated
            print ("expected: " + self.referenceWheel[1][(0+index)])

        for index, spin in enumerate(self.wheelOffset[2]):
            self.wheel[0] = self.wheel[2][1:] + self.wheel[2][0]
            print("First item in self.wheel[2] is " + str(self.wheel[2][0]))
            # Print the expected wheel item to ensure array is moving as anticipated
            print ("expected: " + self.referenceWheel[2][(-1-index)])

        return self.wheel