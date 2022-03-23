import gameSystems

def mainGameLoop(player, wheel):
    gamePlaying = True

    while gamePlaying and player.creditCount > gameSystems.gameSettings.minBet:
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
            
            # take bets from user's wallet, return in 3x2 array of [slot, bet]
            bets = gameSystems.placeBet(slotsBetOn, player)
            
            # Set reference wheel to match spinned wheel so future spins can be properly checked against
            wheel.wheel = wheel.spinWheel()

            # take wheel after spin and bets to get results on the slot user bet on
            result = gameSystems.result(wheel.wheel, bets)

            # calculate results, returns [inSym, midSym, outSym] x3
            resultArray = result.resultList()

            # calculate payout based on bets and result symbols
            payout = gameSystems.payouts(bets, resultArray)

            # returns payouts as [credsIn, credsMid, credsOut]
            winnings = payout.calculatePayouts()

            # Place winnings in player's wallet
            for index, winning in enumerate(winnings):
                # Notify player here of any winning bets they had
                winning = int(winning)
                if winning > 0:
                    print("slot " + str(bets[index][0]) + " won " + str(winning) + " credits!")
                    player.creditCount += winning

            if player.creditCount >= gameSystems.gameSettings.minBet:
                print("Type 1 to play again, 0 to quit")
                if not gameSystems.gameSettings.Debug:
                    userInput = input()
                else:
                    userInput = 1

                if userInput == 1:
                    continue
                elif userInput == 0:
                    gamePlaying = False
            else:
                print("You don't have enough credits to keep playing, game over.")
                exit()
    exit
    return