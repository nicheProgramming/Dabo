import gameSystems

def mainGameLoop():
    print("How many slots would you like to bet on? Type 0 to quit.")
    userInput = input()

    if userInput == 0:
        quit
    elif userInput > 3:
        print ("Too many slots bet on, try again")
    else:
        # store the number of slots bet on from user input
        slotsBetOn = userInput
        # instantiate wheels, later we need to ensure this only happens once per game load
        wheel = gameSystems.wheel()
        # take bets, return in 3x2 array of [slot, bet]
        bets = gameSystems.placeBet(slotsBetOn)
        # spin the wheel
        wheel = wheel.spinWheel()
        # take wheel after spin and bets to get results on the slot user bet on
        result = gameSystems.result(wheel, bets)
        # calculate results, returns [inSym, midSym, outSym] x3
        resultArray = result.resultList()
        # calculate payout based on bets and result symbols
        payout = gameSystems.payouts(bets, resultArray)
        # returns payouts as [credsIn, credsMid, credsOut]
        payout.calculatePayouts()


        