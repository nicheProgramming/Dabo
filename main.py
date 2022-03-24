import gameLoop
import gameTests

# Instantiate player object to track winnings, etc
player = gameLoop.gameSystems.player()
# instantiate wheels
wheel = gameLoop.gameSystems.wheel()

if gameLoop.gameSystems.gameSettings.Debug:
    gameTests.testResults()

gameLoop.mainGameLoop(player, wheel)