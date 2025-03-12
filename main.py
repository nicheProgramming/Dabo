from gameLoop import mainGameLoop
from gameSettings import Debug
from gameSystems import Player, Wheel

# Instantiate player object to track winnings, etc
player = Player()
# instantiate wheels
wheel = Wheel()

if Debug:
    from tests.gameTests import testResults

    testResults()

mainGameLoop(player, wheel)
