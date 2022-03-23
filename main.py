import gameLoop

# Instantiate player object to track winnings, etc
player = gameLoop.gameSystems.player()
# instantiate wheels
wheel = gameLoop.gameSystems.wheel()

gameLoop.mainGameLoop(player, wheel)