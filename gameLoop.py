import gameSystems

def mainGameLoop():
    gamePlaying = True
    # Instantiate player object to track winnings, etc
    player = gameSystems.player()
    # instantiate wheels
    wheel = gameSystems.wheel()

    while gamePlaying:
        # Debug mode check to pass args automatically instead of manually for testing
        if not gameSystems.gameSettings.Debug:
            print("You have " + str(("{:,}".format(player.creditCount))) + " credits.")
            print("How many slots would you like to bet on? Type 0 to quit.")
            userInput = input()
        else:
            userInput = 3

        if userInput == 0:
            quit
        elif int(userInput) > 3:
            print ("Too many slots bet on, try again")
        else:
            # store the number of slots bet on from user input
            slotsBetOn = userInput
            
            # Debug mode check to pass bets automatically for testing
            if not gameSystems.gameSettings.Debug:
                # take bets from user's wallet, return in 3x2 array of [slot, bet]
                bets = gameSystems.placeBet(slotsBetOn, player, wheel)
            else:
                bets = [[0, 50000], [1, 50000], [2, 50000]]
            
            wheel.spunWheel = wheel.spinWheel()

            # take wheel after spin and bets to get results on the slot user bet on
            result = gameSystems.result(wheel.spunWheel, bets)
            # calculate results, returns [inSym, midSym, outSym] x3
            resultArray = result.resultList()

            for index, result in enumerate(resultArray):
                print("Slot " + str(bets[index][0]) + " landed on " + str(result))

            # calculate payout based on bets and result symbols
            payout = gameSystems.payouts(bets, resultArray)
            # returns payouts as [credsIn, credsMid, credsOut]
            winnings = payout.calculatePayouts()

            # Place winnings in player's wallet
            for index, winning in enumerate(winnings):
                # Notify player here of any winning bets they had
                if winning > 0:
                    print("slot " + str(bets[index][0]) + " won " + str(winning) + " credits!")
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