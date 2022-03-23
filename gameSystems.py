import random
import gameSettings

class player(object):
    def __init__(self):
        self.creditCount = gameSettings.maxBet

def placeBet(slotsBetOn, player):
    # Store [slot bet on, amount bet on slot] x 3 
    placedBets = [[-1,-1], [-1,-1], [-1,-1]]
    index = 0
    slotsBetOn = int(slotsBetOn)

    while slotsBetOn > 0 and player.creditCount > 0:
        print("Which slot would you like to bet on?")
        slot = input()

        # Check here if slot is in valid range
        if int(slot) not in gameSettings.bettableSlots:
            print(str(slot) + " is not a valid slot to bet on, please bet on a valid slot.")
            print("Valid slots are: "  + str(gameSettings.bettableSlots))
            continue

        # Check here if slot has already been bet on
        evalIndex = index
        while evalIndex >= 0:
            if placedBets[evalIndex][0] != -1:
                if placedBets[evalIndex][0] == int(slot):
                    print("Slot " + str(slot) + " is already bet on, please choose another.")
                    continue
                else:
                    evalIndex -= 1
            else:
                evalIndex -= 1

        print("How much would you like to bet on slot " + str(slot) + "?")
        bet = int(input())
        
        # Make sure bet is in acceptable range
        if bet < gameSettings.minBet:
            print ("Bet too small, try again.")
        elif bet > gameSettings.maxBet:
            print ("bet too large, try agian.")
        else:
            player.creditCount -= bet
            placedBets[index] = [slot, bet]

        index += 1
        slotsBetOn -= 1 
    # returns 3x2 array of [slot, bet]
    return placedBets

class result(object):
    def __init__(self, wheel, bets):
        # array of all three wheel positions AFTER spin
        self.wheel = wheel
        # 3 x 2 array of [slot, bet], 0 being inner wheel. We only care about slot
        self.bets = bets

    def resultList(self):
        # result must store a 3 x 3 array containing ALL THREE results per slot
        result = [["", "", ""], ["", "", ""], ["", "", ""]]

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

        # Returns 3x3 array with results of symbol results on each bet slot
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
                print("Swirl Dabo!")
                payouts[index] = self.bets[index][1] * 1000
            # If result is three quarks
            elif result[0][0] == "quark" and result[1][0] == "quark" and result[2][0] == "quark":
                # This is a three quark dabo with 200,000% payout
                print ("Quark Dabo!")
                payouts[index] = self.bets[index][1] * 2000
            # If result is three ds9
            elif result[0][0] == "ds9" and result[1][0] == "ds9" and result[2][0] == "ds9":
                # This is a three ds9 dabo with 15,000% payout
                print("Deep space nine Dabo!")
                payouts[index] = self.bets[index][1] * 150
            # If three shapes match 
            elif result[0][0] == result[1][0] and result[1][0] == result[2][0]:
                # If three counts match
                if result[0][1] == result[1][1] and result[1][1] == result[2][1]:
                    # If both colors match
                    if result[1][2] == result[2][2]:
                        # This is a 3x shape 3x count 2x color Dabo with 1000% payout
                        print("Full match Dabo!")
                        payouts[index] = self.bets[index][1] * 10
                    else:
                        # This is a 3x shape 3x count three of a kind with 200% payout
                        print("Three of a Kind!")
                        payouts[index] = self.bets[index][1] * 2
                # If both colors match
                elif result[1][2] == result[2][2]: 
                    # This is 3x shape 2x color three of a kind with 150% payout
                    print("Three of a Kind!")
                    payouts[index] = self.bets[index][1] * 1.5
                # if two counts match
                elif result[0][1] == result[1][1] or result[1][1] == result[2][1] or result[0][1] == result[2][1]:
                    # If both colors match
                    if result[1][2] == result[2][2]:
                        # This is a 3x shape 2x count 2x color three of a kind with 150% payout
                        print("Three of a Kind!")
                        payouts[index] = self.bets[index][1] * 1.5
                    else:
                        # This is a 3x shape 2x count three of a kind with 15 % payout
                        print("Three of a Kind!")
                        payouts[index] = self.bets[index][1] * 1.5
                else:
                    # This is a 3x shape three of a kind with 150% payout
                    print("Three of a Kind!")
                    payouts[index] = self.bets[index][1] * 1.5
            # If three counts match
            elif result[0][1] == result[1][1] and result[1][1] == result[2][1]:
                # if both colors match
                if result[1][2] == result[2][2]: 
                    # This is a 3x count 2x color three of a kind with 200% payout
                    print("Three of a Kind!")
                    payouts[index] = self.bets[index][1] * 2
                else:
                    # This is a 3x count three of a kind with 200% payout
                    print("Three of a Kind!")
                    payouts[index] = self.bets[index][1] * 2
            # If two shapes match
            elif result[0][0] == result[1][0] or result[1][0] == result[2][0] or result[0][0] == result[2][0]:
                # if three counts match
                if result[0][1] == result[1][1] and result[1][1] == result[2][1]:
                    # if both colors match
                    if result[1][2] == result[2][2]: 
                        # This is 2x shape 3x count 2x color three of a kind with 200% payout
                        print("Three of a Kind!")
                        payouts[index] = self.bets[index][1] * 2
                    else:
                        # this is a 2x shape 3x count three of a kind with 200% payout
                        print("Three of a Kind!")
                        payouts[index] = self.bets[index][1] * 2
                # if two counts match
                elif result[0][1] == result[1][1] or result[1][1] == result[2][1] or result[0][1] == result[2][1]:
                    # if both colors match
                    if result[1][2] == result[2][2]: 
                        # This is 2x shape 2x count 2x color two of a kind with 20% payout
                        print("Two of a Kind!")
                        payouts[index] = self.bets[index][1] * .2
                    else:
                        # This is a 2x shape 2x count two of a kind with 15% payout
                        payouts[index] = self.bets[index][1] * .15
                # if both colors match
                elif result[1][2] == result[2][2]: 
                    # This is a 2x shape 2x color two of a kind with 20% payout
                    print("Two of a Kind!")
                    payouts[index] = self.bets[index][1] * .2
                # if two shapes are quarks
                elif (result[0][0] == "quark" and result[1][0] == "quark") or (result[1][0] == "quark" and result[2][0] == "quark") or (result[0][0] == "quark" and result[2][0] == "quark"):
                    # This is a 2x quark two of a kind with 500% payout
                    print("Two of a Kind!")
                    payouts[index] = self.bets[index][1] * 5
                # if two shapes are ds9
                elif (result[0][0] == "ds9" and result[1][0] == "ds9") or (result[1][0] == "ds9" and result[2][0] == "ds9") or (result[0][0] == "ds9" and result[2][0] == "ds9"):
                    # This is a 2x ds9 two of a kind with 400% payout
                    print("Two of a Kind!")
                    payouts[index] = self.bets[index][1] * 4
                else:
                    # This is a 2x shape two of a kind with 10% payout
                    print("Two of a Kind!")
                    payouts[index] = self.bets[index][1] * .1
            # if two count match
            elif result[0][1] == result[1][1] or result[1][1] == result[2][1] or result[0][1] == result[2][1]:
                # if both colors match
                if result[1][2] == result[2][2]: 
                    # This is a 2x count 2x color two of a kind with 20% payout
                    print("Two of a Kind!")
                    payouts[index] = self.bets[index][1] * .2
                else:
                    # This is a 2x count two of a kind with 15% payout
                    print("Two of a Kind!")
                    payouts[index] = self.bets[index][1] * .15
            # if both colors match
            elif result[1][2] == result[2][2]: 
                # This is a 2x color two of a kind with 20% payout
                print("Two of a Kind!")
                payouts[index] = self.bets[index][1] * .2
            else:
                # No winning combo found, no payout. Move on
                print("Sorry, no winning combo on this slot :(")
                continue
        return payouts

class wheel(object):
    def __init__(self):
        self.wheel = self.buildWholeWheel()
        self.wheelOffset = [0, 0, 0]
        # Debug variables
        self.referenceWheel = list(self.wheel)

    def buildOneWheel(self, position):
        # The inner wheel doesn't need to account for color, the others do
        if position == 0:
            # Store shape, then number of shapes
            wheel = [["square", 3],
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
                            ["circle", 2]
            ]
        # Store shape, number of shapes, then color
        elif position == 1:
            wheel = [["triangle", 1, "red"],
                            ["circle", 3, "blue"],
                            ["quark", 1, None],
                            ["triangle", 3, "green"],
                            ["circle", 2, "red"],
                            ["triangle", 2, "green"],
                            ["square", 1, "blue"],
                            ["ds9", 1, None],
                            ["triangle", 3, "red"],
                            ["green", 2, "green"],
                            ["blackHole", 1, None],
                            ["circle", 2, "blue"],
                            ["square", 3, "red"],
                            ["swirl", 1, None],
                            ["circle", 1, "green"],
                            ["triangle", 3, "blue"],
                            ["circle", 1, "red"],
                            ["triangle", 1, "green"],
                            ["square", 2, "blue"],
                            ["ds9", 1, None],
                            ["square", 1, "red"],
                            ["square", 3, "blue"],
                            ["circle", 3, "green"],
                            ["square", 2, "red"],
                            ["blackHole", 1, None],
                            ["circle", 1, "blue"],
                            ["square", 3, "green"],
                            ["triangle", 2, "red"],
                            ["triangle", 1, "blue"],
                            ["swirl", 1, None],
                            ["circle", 3, "red"],
                            ["square", 1, "green"],
                            ["ds9", 1, None],
                            ["triangle", 2, "blue"],
                            ["blackHole", 1, None],
                            ["circle", 2, "green"]
            ]
        elif position == 2:
            # Store shape, number of shapes, then color
            wheel = [["blackHole", 1, None],
                            ["circle", 2, "green"],
                            ["triangle", 1, "red"],
                            ["circle", 3, "blue"],
                            ["quark", 1, None],
                            ["triangle", 3, "green"],
                            ["circle", 2, "red"],
                            ["triangle", 2, "green"],
                            ["square", 1, "blue"],
                            ["ds9", 1, None],
                            ["triangle", 3, "red"],
                            ["square", 2, "green"],
                            ["blackHole", 1, None],
                            ["circle", 2, "blue"],
                            ["square", 3, "red"],
                            ["swirl", 1, None],
                            ["circle", 1, "green"],
                            ["triangle", 3, "blue"],
                            ["circle", 1, "red"],
                            ["triangle", 1, "green"],
                            ["square", 2, "blue"],
                            ["ds9", 1, None],
                            ["square", 1, "red"],
                            ["square", 3, "blue"],
                            ["circle", 3, "green"],
                            ["square", 2, "red"],
                            ["blackHole", 1, None],
                            ["circle", 1, "blue"],
                            ["square", 3, "green"],
                            ["triangle", 2, "red"],
                            ["triangle", 1, "blue"],
                            ["swirl", 1, None],
                            ["circle", 3, "red"],
                            ["square", 1, "green"],
                            ["ds9", 1, None],
                            ["triangle", 2, "blue"]
            ]
        return wheel
    
    def buildWholeWheel(self):
        result = [[], [], []]

        result[0] = self.buildOneWheel(0)
        result[1] = self.buildOneWheel(1)
        result[2] = self.buildOneWheel(2)

        return result
    
    def spinWheel(self):
        self.wheelOffset = [random.randrange(0, 35), random.randrange(0, 35), random.randrange(0, 35)]
        index = 0

        while self.wheelOffset[0] > 0:
            # Put first item in array at the end of the array
            self.wheel[0] = self.wheel[0][1:] + [self.wheel[0][0]]
            self.wheelOffset[0] -= 1
            
            # make sure last item in wheel matches item in reference wheel at offset iteration index (index of how many times offset has been applied)
            if self.wheel[0][-1] != self.referenceWheel[0][index]:
                print("!!!wheel not spinning properly!!!")
                print("Last item in self.wheel[0] is " + str(self.wheel[0][-1]))
                print ("expected: " + str(self.referenceWheel[0][index]))
                exit()
                
            index += 1

        # must be reset after each wheel spin
        index = 0

        while self.wheelOffset[1] > 0:
            # Put last item of array in first place
            # This is reversed on purpose, this wheel spins counter clockwise, unlike the other two wheels 
            self.wheel[1] = [self.wheel[1][-1]] + self.wheel[1][:-1]
            self.wheelOffset[1] -= 1

            # make sure first item in wheel matches item in reference wheel at reverse offset iteration index (index of how many times offset has been applied)
            if self.wheel[1][0] != self.referenceWheel[1][-index-1]:
                print("!!!wheel not spinning properly!!!")
                print("First item in self.wheel[1] is " + str(self.wheel[1][0]))
                print ("expected: " + str(self.referenceWheel[1][-index-1]))
                exit()

            index += 1

            # print("First item in self.wheel[1] is " + str(self.wheel[1][0]))
            # # Print the expected wheel item to ensure array is moving as anticipated
            # print ("expected: " + self.referenceWheel[1][(0+index)])

        # must be reset after each wheel spin
        index = 0

        while self.wheelOffset[2] > 0:
            # Put first item in array at the end of the array
            self.wheel[2] = self.wheel[2][1:] + [self.wheel[2][0]]
            self.wheelOffset[2] -= 1
            
            # make sure last item in wheel matches item in reference wheel at offset iteration index (index of how many times offset has been applied)
            if self.wheel[2][-1] != self.referenceWheel[2][index]:
                print("!!!wheel not spinning properly!!!")
                print("Last item in self.wheel[2] is " + str(self.wheel[2][-1]))
                print ("expected: " + str(self.referenceWheel[2][(index)]))
                exit()
                
            index += 1
        
        return self.wheel