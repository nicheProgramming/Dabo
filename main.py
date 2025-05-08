from gameLoop import mainGameLoop
from gameSettings import Debug

if Debug:
    from tests.gameTests import testResults

    testResults()

mainGameLoop()
