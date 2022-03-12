import gameSystems

def mainGameLoop():
    print("How many slots would you like to bet on? Type 0 to quit.")
    userInput = input()

    if userInput == 0:
        quit
    else:
        slotsBetOn = userInput
        
        bets = gameSystems.placeBet(slotsBetOn)

        