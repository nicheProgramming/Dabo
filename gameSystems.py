import random
import gameSettings

minBet = 100
maxBet = 1000000

class player(object):
    def __init__(self):
        self.creditCount = maxBet

def placeBet(slotsBetOn, player):
    # Store [slot bet on, amount bet on slot] x 3 
    placedBets = [[], [], []]
    index = 0

    while int(slotsBetOn) > 0 and player.creditCount > 0:
        print("Which slot would you like to bet on?")
        slot = input()

        # Check here if slot is in valid range

        print("How much would you like to bet on slot " + str(slot) + "?")
        bet = input()
        
        # Make sure bet is in acceptable range
        if bet < minBet:
            print ("Bet too small, try again.")
        elif bet > maxBet:
            print ("bet too large, try agian.")
        else:
            player.creditCount -= bet
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
        self.bets = bets
        # Should be a 1x3 to 3x3 array, three symbols per slot, UP to three slots bet on
        self.results = results
    
    def calculatePayouts(self):
        payouts = [0, 0, 0]

        # result iterates through results (each loop assesses a single ring's result array)
        for index, result in enumerate(self.results):
            # If result is three swirls
            if result[0][0] == "swirl" and result[1][0] == "swirl" and result[2][0] == "swirl":
                # This is a three swirl dabo with 100,000% payout
                payouts[index] = self.bets[index][1] * 1000
            # If result is three quarks
            elif result[0][0] == "quark" and result[1][0] == "quark" and result[2][0] == "quark":
                # This is a three quark dabo with 200,000% payout
                payouts[index] = self.bets[index][1] * 2000
            # If result is three ds9
            elif result[0][0] == "ds9" and result[1][0] == "ds9" and result[2][0] == "ds9":
                # This is a three ds9 dabo with 15,000% payout
                payouts[index] = self.bets[index][1] * 150
            # If three shapes match 
            elif result[0][0] == result[1][0] and result[1][0] == result[2][0]:
                # If three counts match
                if result[0][1] == result[1][1] and result[1][1] == result[2][1]:
                    # If both colors match
                    if result[1][2] == result[2][2]:
                        # This is a 3x shape 3x count 2x color Dabo with 1000% payout
                        payouts[index] = self.bets[index][1] * 10
                    else:
                        # This is a 3x shape 3x count three of a kind with 200% payout
                        payouts[index] = self.bets[index][1] * 2
                # If both colors match
                elif result[1][2] == result[2][2]: 
                    # This is 3x shape 2x color three of a kind with 150% payout
                    payouts[index] = self.bets[index][1] * 1.5
                # if two counts match
                elif result[0][1] == result[1][1] or result[1][1] == result[2][1] or result[0][1] == result[2][1]:
                    # If both colors match
                    if result[1][2] == result[2][2]:
                        # This is a 3x shape 2x count 2x color three of a kind with 150% payout
                        payouts[index] = self.bets[index][1] * 1.5
                    else:
                        # This is a 3x shape 2x count three of a kind with 15 % payout
                        payouts[index] = self.bets[index][1] * 1.5
                else:
                    # This is a 3x shape three of a kind with 150% payout
                    payouts[index] = self.bets[index][1] * 1.5
            # If three counts match
            elif result[0][1] == result[1][1] and result[1][1] == result[2][1]:
                # if both colors match
                if result[1][2] == result[2][2]: 
                    # This is a 3x count 2x color three of a kind with 200% payout
                    payouts[index] = self.bets[index][1] * 2
                else:
                    # This is a 3x count three of a kind with 200% payout
                    payouts[index] = self.bets[index][1] * 2
            # If two shapes match
            elif result[0][0] == result[1][0] or result[1][0] == result[2][0] or result[0][0] == result[2][0]:
                # if three counts match
                if result[0][1] == result[1][1] and result[1][1] == result[2][1]:
                    # if both colors match
                    if result[1][2] == result[2][2]: 
                        # This is 2x shape 3x count 2x color three of a kind with 200% payout
                        payouts[index] = self.bets[index][1] * 2
                    else:
                        # this is a 2x shape 3x count three of a kind with 200% payout
                        payouts[index] = self.bets[index][1] * 2
                # if two counts match
                elif result[0][1] == result[1][1] or result[1][1] == result[2][1] or result[0][1] == result[2][1]:
                    # if both colors match
                    if result[1][2] == result[2][2]: 
                        # This is 2x shape 2x count 2x color two of a kind with 20% payout
                        payouts[index] = self.bets[index][1] * .2
                    else:
                        # This is a 2x shape 2x count two of a kind with 15% payout
                        payouts[index] = self.bets[index][1] * .15
                # if both colors match
                elif result[1][2] == result[2][2]: 
                    # This is a 2x shape 2x color two of a kind with 20% payout
                    payouts[index] = self.bets[index][1] * .2
                # if two shapes are quarks
                elif (result[0][0] == "quark" and result[1][0] == "quark") or (result[1][0] == "quark" and result[2][0] == "quark") or (result[0][0] == "quark" and result[2][0] == "quark"):
                    # This is a 2x quark two of a kind with 500% payout
                    payouts[index] = self.bets[index][1] * 5
                # if two shapes are ds9
                elif (result[0][0] == "ds9" and result[1][0] == "ds9") or (result[1][0] == "ds9" and result[2][0] == "ds9") or (result[0][0] == "ds9" and result[2][0] == "ds9"):
                    # This is a 2x ds9 two of a kind with 400% payout
                    payouts[index] = self.bets[index][1] * 4
                else:
                    # This is a 2x shape two of a kind with 10% payout
                    payouts[index] = self.bets[index][1] * .1
            # if two count match
            elif result[0][1] == result[1][1] or result[1][1] == result[2][1] or result[0][1] == result[2][1]:
                # if both colors match
                if result[1][2] == result[2][2]: 
                    # This is a 2x count 2x color two of a kind with 20% payout
                    payouts[index] = self.bets[index][1] * .2
                else:
                    # This is a 2x count two of a kind with 15% payout
                    payouts[index] = self.bets[index][1] * .15
                #RESUME WORK HERE, YOU NEED TO EVALUATE LARGER MATCHES BEFORE SMALLER ONES
            # if both colors match
            elif result[1][2] == result[2][2]: 
                # This is a 2x color two of a kind with 20% payout
                    payouts[index] = self.bets[index][1] * .2
            else:
                # No winning combo found, no payout. Move on
                    continue
        return payouts


class wheel(object):
    def __init__(self):
        self.buildWheel = gameSettings.instantiateWheel()
        self.wheel = self.buildWheel.buildWholeWheel()
        self.wheelOffset = [0, 0, 0]
        # Debug variables
        self.referenceWheel = self.buildWheel.buildWholeWheel()
    
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