import gameSystems

def testPayouts(player, wheel):
    slotsBetOn = 3
    bets = [[31, 100], [7, 100], [19, 100]]
    wheel.wheel = wheel.spinWheel()
    result = gameSystems.result(wheel.wheel, bets)
    resultArray = result.resultList()

    return