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
    numOfTestSpins = 100000
    wheel = gameSystems.wheel()
    player = gameSystems.player()

    # Spin the wheel numOfTestSpins times to get stats on results
    while numOfTestSpins > 0:
        slot1 = random.choice(gameSystems.gameSettings.bettableSlots)
        slot2 = random.choice(gameSystems.gameSettings.bettableSlots)
        slot3 = random.choice(gameSystems.gameSettings.bettableSlots)
        bet = random.randrange(gameSystems.gameSettings.minBet, gameSystems.gameSettings.maxBet)

        # example bets = [[31, 100], [7, 100], [19, 100]]
        bets = [[slot1, bet], [slot2, bet], [slot3, bet]]
        wheel.wheel = wheel.spinWheel()
        result = gameSystems.result(wheel.wheel, bets)
        resultArray = result.resultList()
        payout = gameSystems.payouts(bets, resultArray)
        payout.calculatePayouts()
        numOfTestSpins -= 1

    # Expected probability of a given result in percentage
    expected_SwirlDabo = .02
    expected_QuarkDabo = .01
    expected_ds9Dabos = .06
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

    # Calculate actual result percentages    
    actual_swirlDabos = round(gameSystems.gameSettings.swirlDabos / gameSystems.gameSettings.numOfSpins, 2)
    actual_quarkDabos = round(gameSystems.gameSettings.quarkDabos / gameSystems.gameSettings.numOfSpins, 2)
    actual_ds9Dabos = round(gameSystems.gameSettings.ds9Dabos / gameSystems.gameSettings.numOfSpins, 2) 
    actual_3shape3count2colorDabos = round(gameSystems.gameSettings._3shape3count2colorDabos / gameSystems.gameSettings.numOfSpins, 2)

    actual_3shape3count3OAK = round(gameSystems.gameSettings._3shape3count3OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_3shape2color3OAK = round(gameSystems.gameSettings._3shape2color3OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_3shape2count2color3OAK = round(gameSystems.gameSettings._3shape2count2color3OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_3shape2count3OAK = round(gameSystems.gameSettings._3shape2count3OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_3shape3OAK = round(gameSystems.gameSettings._3shape3OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_3count2color3OAK = round(gameSystems.gameSettings._3count2color3OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_3count3OAK = round(gameSystems.gameSettings._3count3OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2shape3count2color3OAK = round(gameSystems.gameSettings._2shape3count2color3OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2shape3count3OAK = round(gameSystems.gameSettings._2shape3count3OAK / gameSystems.gameSettings.numOfSpins, 2)

    actual_2shape2count2color2OAK = round(gameSystems.gameSettings._2shape2count2color2OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2shape2count2OAK = round(gameSystems.gameSettings._2shape2count2OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2shape2color2OAK = round(gameSystems.gameSettings._2shape2color2OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2quark2OAK = round(gameSystems.gameSettings._2quark2OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2ds92OAK = round(gameSystems.gameSettings._2ds92OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2shape2OAK = round(gameSystems.gameSettings._2shape2OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2count2color2OAK = round(gameSystems.gameSettings._2count2color2OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2count2OAK = round(gameSystems.gameSettings._2count2OAK / gameSystems.gameSettings.numOfSpins, 2)
    actual_2color2OAK = round(gameSystems.gameSettings._2color2OAK / gameSystems.gameSettings.numOfSpins, 2)

    actualNoPayout = round(gameSystems.gameSettings.noPayout / gameSystems.gameSettings.numOfSpins, 2)

    # Compare expected vs actual results
    if actual_swirlDabos != expected_SwirlDabo:
        print("Actual swirl dabo: " + str(actual_swirlDabos) + " | Expected: " + str(expected_SwirlDabo))
    if actual_quarkDabos != expected_QuarkDabo:
        print("Actual quark dabo: " + str(actual_quarkDabos) + " | Expected: " + str(expected_QuarkDabo))
    if actual_ds9Dabos != expected_ds9Dabos:
        print("Actual ds9 dabo: " + str(actual_ds9Dabos) + " | Expected: " + str(expected_ds9Dabos))
    if actual_3shape3count2colorDabos != expected_3shape3count2colorDabos:
        print("Actual 3shape3count2color dabo: " + str(actual_3shape3count2colorDabos) + " | Expected: " + str(expected_3shape3count2colorDabos))

    if actual_3shape3count3OAK != expected_3shape3count3OAK:
        print("Actual 3shape3count3OAK: " + str(actual_3shape3count3OAK) + " | Expected: " + str(expected_3shape3count3OAK))
    if actual_3shape2color3OAK != expected_3shape2color3OAK:
        print("Actual 3shape2color3OAK: " + str(actual_3shape2color3OAK) + " | Expected: " + str(expected_3shape2color3OAK))
    if actual_3shape2count2color3OAK != expected_3shape2count2color3OAK:
        print("Actual 3shape2count2color3OAK: " + str(actual_3shape2count2color3OAK) + " | Expected: " + str(expected_3shape2count2color3OAK))
    if actual_3shape2count3OAK != expected_3shape2count3OAK:
        print("Actual 3shape2count3OAK: " + str(actual_3shape2count3OAK) + " | Expected: " + str(expected_3shape2count3OAK))
    if actual_3shape3OAK != expected_3shape3OAK:
        print("Actual _3shape3OAK: " + str(actual_3shape3OAK) + " | Expected: " + str(expected_3shape3OAK))
    if actual_3count2color3OAK != expected_3count2color3OAK:
        print("Actual 3count2color3OAK: " + str(actual_3count2color3OAK) + " | Expected: " + str(expected_3count2color3OAK))
    if actual_3count3OAK != expected_3count3OAK:
        print("Actual 3count3OAK: " + str(actual_3count3OAK) + " | Expected: " + str(expected_3count3OAK))
    if actual_2shape3count2color3OAK != expected_2shape3count2color3OAK:
        print("Actual 2shape3count2color3OAK: " + str(actual_2shape3count2color3OAK) + " | Expected: " + str(expected_2shape3count2color3OAK))
    if actual_2shape3count3OAK != expected_2shape3count3OAK:
        print("Actual 2shape3count3OAK: " + str(actual_2shape3count3OAK) + " | Expected: " + str(expected_2shape3count3OAK))

    if actual_2shape2count2color2OAK != expected_2shape2count2color2OAK:
        print("Actual 2shape2count2color2OAK: " + str(actual_2shape2count2color2OAK) + " | Expected: " + str(expected_2shape2count2color2OAK))
    if actual_2shape2count2OAK != expected_2shape2count2OAK:
        print("Actual 2shape2count2OAK: " + str(actual_2shape2count2OAK) + " | Expected: " + str(expected_2shape2count2OAK))
    if actual_2shape2color2OAK != expected_2shape2color2OAK:
        print("Actual 2shape2color2OAK: " + str(actual_2shape2color2OAK) + " | Expected: " + str(expected_2shape2color2OAK))
    if actual_2quark2OAK != expected_2quark2OAK:
        print("Actual 2quark2OAK: " + str(actual_2quark2OAK) + " | Expected: " + str(expected_2quark2OAK))
    if actual_2ds92OAK != expected_2ds92OAK:
        print("Actual 2ds92OAK: " + str(actual_2ds92OAK) + " | Expected: " + str(expected_2ds92OAK))
    if actual_2count2color2OAK != expected_2count2color2OAK:
        print("Actual 2count2color2OAK: " + str(actual_2count2color2OAK) + " | Expected: " + str(expected_2count2color2OAK))
    if actual_2count2OAK != expected_2count2OAK:
        print("Actual 2count2OAK: " + str(actual_2count2OAK) + " | Expected: " + str(expected_2count2OAK))
    if actual_2color2OAK != expected_2color2OAK:
        print("Actual 2color2OAK: " + str(actual_2color2OAK) + " | Expected: " + str(expected_2color2OAK))
    
    if actualNoPayout != expectedNoPayout:
        print("Actual noPayout: " + str(actualNoPayout) + " | Expected: " + str(expectedNoPayout))

    exit()

    return