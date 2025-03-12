import random

from gameSettings import (
    _2color2OAK,
    _2count2color2OAK,
    _2count2OAK,
    _2ds92OAK,
    _2quark2OAK,
    _2shape2color2OAK,
    _2shape2count2color2OAK,
    _2shape2count2OAK,
    _2shape2OAK,
    _2shape3count2color3OAK,
    _2shape3count3OAK,
    _3count2color3OAK,
    _3count3OAK,
    _3shape2color3OAK,
    _3shape2count2color3OAK,
    _3shape2count3OAK,
    _3shape3count2colorDabos,
    _3shape3count3OAK,
    _3shape3OAK,
    bettableSlots,
    ds9Dabos,
    maxBet,
    minBet,
    noPayout,
    quarkDabos,
    swirlDabos,
)
from gameSystems import Payouts, Player, Result, Wheel

# TODO: Test that each wheel is 36 shapes long


def testPayouts(player: Player, wheel: Wheel):
    slotsBetOn = 3
    bets = [[31, 100], [7, 100], [19, 100]]
    wheel.wheel = wheel.spinWheel()
    result = result(wheel.wheel, bets)
    resultArray = result.resultList()

    return


def testResults():
    numOfTestSpins = 100000
    wheel = Wheel()
    player = Player()

    # Spin the wheel numOfTestSpins times to get stats on results
    while numOfTestSpins > 0:
        slot1 = random.choice(bettableSlots)
        slot2 = random.choice(bettableSlots)
        slot3 = random.choice(bettableSlots)
        bet = random.randrange(minBet, maxBet)

        # example bets = [[31, 100], [7, 100], [19, 100]]
        bets = [[slot1, bet], [slot2, bet], [slot3, bet]]
        wheel.wheel = wheel.spinWheel(player)
        result = Result(wheel.wheel, bets)
        resultArray = result.resultList()
        payout = Payouts(bets, resultArray)
        payout.calculatePayouts()
        numOfTestSpins -= 1

    numOfSpins = player.numOfSpins

    # Expected probability of a given result in percentage
    expected_SwirlDabo = 0.02
    expected_QuarkDabo = 0.01
    expected_ds9Dabos = 0.06
    expected_3shape3count2colorDabos = 1.68

    expected_3shape3count3OAK = 0.58
    expected_3shape2color3OAK = 0.35
    expected_3shape2count2color3OAK = 2.66
    expected_3shape2count3OAK = 2.55
    expected_3shape3OAK = 0.69
    expected_3count2color3OAK = 0.35
    expected_3count3OAK = 0.69
    expected_2shape3count2color3OAK = 2.66
    expected_2shape3count3OAK = 2.55

    expected_2shape2count2color2OAK = 11.58
    expected_2shape2count2OAK = 20.03
    expected_2shape2color2OAK = 2.89
    expected_2quark2OAK = 0.23
    expected_2ds92OAK = 1.91
    expected_2shape2OAK = 10.65
    expected_2count2color2OAK = 2.89
    expected_2count2OAK = 10.65
    expected_2color2OAK = 2.31

    expectedNoPayout = 22.02

    # Calculate actual result percentages
    actual_swirlDabos = round(swirlDabos / numOfSpins, 2)
    actual_quarkDabos = round(quarkDabos / numOfSpins, 2)
    actual_ds9Dabos = round(ds9Dabos / numOfSpins, 2)
    actual_3shape3count2colorDabos = round(
        _3shape3count2colorDabos / numOfSpins,
        2,
    )

    actual_3shape3count3OAK = round(
        _3shape3count3OAK / numOfSpins,
        2,
    )
    actual_3shape2color3OAK = round(
        _3shape2color3OAK / numOfSpins,
        2,
    )
    actual_3shape2count2color3OAK = round(
        _3shape2count2color3OAK / numOfSpins,
        2,
    )
    actual_3shape2count3OAK = round(
        _3shape2count3OAK / numOfSpins,
        2,
    )
    actual_3shape3OAK = round(_3shape3OAK / numOfSpins, 2)
    actual_3count2color3OAK = round(
        _3count2color3OAK / numOfSpins,
        2,
    )
    actual_3count3OAK = round(_3count3OAK / numOfSpins, 2)
    actual_2shape3count2color3OAK = round(
        _2shape3count2color3OAK / numOfSpins,
        2,
    )
    actual_2shape3count3OAK = round(
        _2shape3count3OAK / numOfSpins,
        2,
    )

    actual_2shape2count2color2OAK = round(
        _2shape2count2color2OAK / numOfSpins,
        2,
    )
    actual_2shape2count2OAK = round(
        _2shape2count2OAK / numOfSpins,
        2,
    )
    actual_2shape2color2OAK = round(
        _2shape2color2OAK / numOfSpins,
        2,
    )
    actual_2quark2OAK = round(_2quark2OAK / numOfSpins, 2)
    actual_2ds92OAK = round(_2ds92OAK / numOfSpins, 2)
    actual_2shape2OAK = round(_2shape2OAK / numOfSpins, 2)
    actual_2count2color2OAK = round(
        _2count2color2OAK / numOfSpins,
        2,
    )
    actual_2count2OAK = round(_2count2OAK / numOfSpins, 2)
    actual_2color2OAK = round(_2color2OAK / numOfSpins, 2)

    actualNoPayout = round(noPayout / numOfSpins, 2)

    # Compare expected vs actual results
    if actual_swirlDabos != expected_SwirlDabo:
        print(
            "Actual swirl dabo: "
            + str(actual_swirlDabos)
            + " | Expected: "
            + str(expected_SwirlDabo)
        )
    if actual_quarkDabos != expected_QuarkDabo:
        print(
            "Actual quark dabo: "
            + str(actual_quarkDabos)
            + " | Expected: "
            + str(expected_QuarkDabo)
        )
    if actual_ds9Dabos != expected_ds9Dabos:
        print(
            "Actual ds9 dabo: "
            + str(actual_ds9Dabos)
            + " | Expected: "
            + str(expected_ds9Dabos)
        )
    if actual_3shape3count2colorDabos != expected_3shape3count2colorDabos:
        print(
            "Actual 3shape3count2color dabo: "
            + str(actual_3shape3count2colorDabos)
            + " | Expected: "
            + str(expected_3shape3count2colorDabos)
        )

    if actual_3shape3count3OAK != expected_3shape3count3OAK:
        print(
            "Actual 3shape3count3OAK: "
            + str(actual_3shape3count3OAK)
            + " | Expected: "
            + str(expected_3shape3count3OAK)
        )
    if actual_3shape2color3OAK != expected_3shape2color3OAK:
        print(
            "Actual 3shape2color3OAK: "
            + str(actual_3shape2color3OAK)
            + " | Expected: "
            + str(expected_3shape2color3OAK)
        )
    if actual_3shape2count2color3OAK != expected_3shape2count2color3OAK:
        print(
            "Actual 3shape2count2color3OAK: "
            + str(actual_3shape2count2color3OAK)
            + " | Expected: "
            + str(expected_3shape2count2color3OAK)
        )
    if actual_3shape2count3OAK != expected_3shape2count3OAK:
        print(
            "Actual 3shape2count3OAK: "
            + str(actual_3shape2count3OAK)
            + " | Expected: "
            + str(expected_3shape2count3OAK)
        )
    if actual_3shape3OAK != expected_3shape3OAK:
        print(
            "Actual _3shape3OAK: "
            + str(actual_3shape3OAK)
            + " | Expected: "
            + str(expected_3shape3OAK)
        )
    if actual_3count2color3OAK != expected_3count2color3OAK:
        print(
            "Actual 3count2color3OAK: "
            + str(actual_3count2color3OAK)
            + " | Expected: "
            + str(expected_3count2color3OAK)
        )
    if actual_3count3OAK != expected_3count3OAK:
        print(
            "Actual 3count3OAK: "
            + str(actual_3count3OAK)
            + " | Expected: "
            + str(expected_3count3OAK)
        )
    if actual_2shape3count2color3OAK != expected_2shape3count2color3OAK:
        print(
            "Actual 2shape3count2color3OAK: "
            + str(actual_2shape3count2color3OAK)
            + " | Expected: "
            + str(expected_2shape3count2color3OAK)
        )
    if actual_2shape3count3OAK != expected_2shape3count3OAK:
        print(
            "Actual 2shape3count3OAK: "
            + str(actual_2shape3count3OAK)
            + " | Expected: "
            + str(expected_2shape3count3OAK)
        )

    if actual_2shape2count2color2OAK != expected_2shape2count2color2OAK:
        print(
            "Actual 2shape2count2color2OAK: "
            + str(actual_2shape2count2color2OAK)
            + " | Expected: "
            + str(expected_2shape2count2color2OAK)
        )
    if actual_2shape2count2OAK != expected_2shape2count2OAK:
        print(
            "Actual 2shape2count2OAK: "
            + str(actual_2shape2count2OAK)
            + " | Expected: "
            + str(expected_2shape2count2OAK)
        )
    if actual_2shape2color2OAK != expected_2shape2color2OAK:
        print(
            "Actual 2shape2color2OAK: "
            + str(actual_2shape2color2OAK)
            + " | Expected: "
            + str(expected_2shape2color2OAK)
        )
    if actual_2quark2OAK != expected_2quark2OAK:
        print(
            "Actual 2quark2OAK: "
            + str(actual_2quark2OAK)
            + " | Expected: "
            + str(expected_2quark2OAK)
        )
    if actual_2ds92OAK != expected_2ds92OAK:
        print(
            "Actual 2ds92OAK: "
            + str(actual_2ds92OAK)
            + " | Expected: "
            + str(expected_2ds92OAK)
        )
    if actual_2count2color2OAK != expected_2count2color2OAK:
        print(
            "Actual 2count2color2OAK: "
            + str(actual_2count2color2OAK)
            + " | Expected: "
            + str(expected_2count2color2OAK)
        )
    if actual_2count2OAK != expected_2count2OAK:
        print(
            "Actual 2count2OAK: "
            + str(actual_2count2OAK)
            + " | Expected: "
            + str(expected_2count2OAK)
        )
    if actual_2color2OAK != expected_2color2OAK:
        print(
            "Actual 2color2OAK: "
            + str(actual_2color2OAK)
            + " | Expected: "
            + str(expected_2color2OAK)
        )

    if actualNoPayout != expectedNoPayout:
        print(
            "Actual noPayout: "
            + str(actualNoPayout)
            + " | Expected: "
            + str(expectedNoPayout)
        )

    exit()

    return
