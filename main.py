import gameLoop

# Instantiate player object to track winnings, etc
player = gameLoop.gameSystems.player()
# instantiate wheels
wheel = gameLoop.gameSystems.wheel()

wheel.referenceWheel = wheel.buildWholeWheel()

gameLoop.mainGameLoop(player, wheel)