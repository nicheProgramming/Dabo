import gameSystems

def mainGameLoop():
    print("How many slots would you like to bet on? Type 0 to quit.")
    userInput = input()

    if userInput == 0:
        quit
    else:
        slotsBetOn = userInput
        
        while slotsBetOn > 0:
            print("Which slot would you like to bet on?")
            slot = input()
            slotsBetOn -= 1

            print("How much would you like to bet on slot " + str(slot) + "?")
            bet = input()

            if bet < gameSystems.minBet:
                print ("Bet too small, try again.")
            elif bet > gameSystems.maxBet:
                print ("bet too large, try agian.")
            else:
                break

        