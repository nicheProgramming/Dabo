import gameSystems

def mainGameLoop():
    print("How many slots would you like to bet on? Type 0 to quit.")
    userInput = input()

    if userInput == 0:
        quit
    elif userInput > 3:
        print ("Too many slots bet on, try again")
    else:
        slotsBetOn = userInput
        wheel = gameSystems.wheel()
        bets = gameSystems.placeBet(slotsBetOn)
        wheel = wheel.spinWheel()
        result = gameSystems.result(wheel, bets)
        resultArray = result.resultList()
        payout = gameSystems.payouts(bets, resultArray)


        