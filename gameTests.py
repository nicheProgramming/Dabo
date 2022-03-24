import random
import gameSystems

def testPayouts(player, wheel):
    slotsBetOn = 3
    bets = [[31, 100], [7, 100], [19, 100]]
    wheel.wheel = wheel.spinWheel()
    result = gameSystems.result(wheel.wheel, bets)
    resultArray = result.resultList()

    return

def testResults():
    numOfTestSpins = 10000
    wheel = gameSystems.wheel()
    player = gameSystems.player()

    # Spin the wheel numOfTestSpins times to get stats on results
    while numOfTestSpins > 0:
        slot1 = random.choice(gameSystems.gameSettings.bettableSlots)
        slot2 = random.choice(gameSystems.gameSettings.bettableSlots)
        slot3 = random.choice(gameSystems.gameSettings.bettableSlots)
        bet = random.randrange(gameSystems.gameSettings.minBet, gameSystems.gameSettings.maxBet)

        bets = [[]]
        wheel.wheel = wheel.spinWheel()
        result = gameSystems.result(wheel.wheel, bets)
        resultArray = result.resultList()
        numOfTestSpins -= 1

    # Expected probability of a given result in percentage
    expectedSwirlDabo = .02
    expectedQuarkDabo = .01
    expectedDa9Dabo = .06
    expected_3shape3count2colorDabos = 1.68

    expected_3shape3count3OAK = .58
    expected_3shape2color3OAK = .35
    expected_3shape2count2color3OAK = 2.66
    expected_3shape2count3OAK = 2.55
    expected_3shape3OAK = .69
    expected_3count2color3OAK = .35
    expected_3count3OAK = .69
    expected_2shape3count2color3OAK = 2.66
    expected_2shape3count3OAK = 2.55

    expected_2shape2count2color2OAK = 11.58
    expected_2shape2count2OAK = 20.03
    expected_2shape2color2OAK = 2.89
    expected_2quark2OAK = .23
    expected_2ds92OAK = 1.91
    expected_2shape2OAK = 10.65
    expected_2count2color2OAK = 2.89
    expected_2count2OAK = 10.65
    expected_2color2OAK = 2.31
    
    expectedNoPayout = 22.02

    # Evaluate spin results versus expected values
    
    return