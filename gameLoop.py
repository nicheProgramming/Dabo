import gameSystems

def mainGameLoop():
    gamePlaying = True
    # Instantiate player object to track winnings, etc
    player = gameSystems.player()
    # instantiate wheels
    wheel = gameSystems.wheel()

    while gamePlaying:
        print("You have " + str(("{:,}".format(player.creditCount))) + " credits.")
        print("How many slots would you like to bet on? Type 0 to quit.")
        userInput = input()

        if userInput == 0:
            quit
        elif int(userInput) > 3:
            print ("Too many slots bet on, try again")
        else:
            # store the number of slots bet on from user input
            slotsBetOn = userInput
            # take bets from user's wallet, return in 3x2 array of [slot, bet]
            bets = gameSystems.placeBet(slotsBetOn, player, wheel)
            # spin the wheel
            wheel = wheel.spinWheel()
            # take wheel after spin and bets to get results on the slot user bet on
            result = gameSystems.result(wheel, bets)
            # calculate results, returns [inSym, midSym, outSym] x3
            resultArray = result.resultList()

            # Notify player here of any winning bets they had

            # calculate payout based on bets and result symbols
            payout = gameSystems.payouts(bets, resultArray)
            # returns payouts as [credsIn, credsMid, credsOut]
            winnings = payout.calculatePayouts()
            # Place winnings in player's wallet
            for winning in winnings:
                player.creditCount += winning

            if player.creditCount > 0:
                print("Type 1 to play again, 0 to quit")
                userInput = input()

                if userInput == 1:
                    continue
                elif userInput == 0:
                    gamePlaying = False
    exit
    return