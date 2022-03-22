import gameSystems

def mainGameLoop(player, wheel):
    gamePlaying = True

    while gamePlaying:
        # Debug mode check to pass args automatically instead of manually for testing
        if not gameSystems.gameSettings.Debug:
            print("You have " + str(("{:,}".format(player.creditCount))) + " credits.")
            print("How many slots would you like to bet on? Type 0 to quit.")
            userInput = input()
        else:
            print("You have " + str(("{:,}".format(player.creditCount))) + " credits.")
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
                bets = gameSystems.placeBet(slotsBetOn, player)
            else:
                bets = [[0, 50000], [1, 50000], [2, 50000]]
            
            # Set reference wheel to match spinned wheel so future spins can be properly checked against
            wheel.wheel = wheel.spinWheel()

            # Set ref wheel to VALUE, no OBJECT of wheel after spin for continuitiy
            wheel.referenceWheel = list(wheel.wheel)

            # take wheel after spin and bets to get results on the slot user bet on
            result = gameSystems.result(wheel.wheel, bets)
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
                if not gameSystems.gameSettings.Debug:
                    userInput = input()
                else:
                    userInput = 1

                if userInput == 1:
                    continue
                elif userInput == 0:
                    gamePlaying = False
    exit
    return