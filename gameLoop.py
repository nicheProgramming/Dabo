from sys import exit as sys_exit

from game_classes import Player, Wheel
from gameSettings import Debug, minBet
from gameSystems import Payouts, Result


def mainGameLoop():
    game_playing = True
    # Instantiate player object to track winnings, etc
    player = Player()
    # instantiate wheels
    wheel = Wheel()

    while game_playing and player.credits_count > minBet:
        # Debug mode check to pass args automatically instead of manually for testing
        if not Debug:
            player.print_credits()

            user_input: int = player.get_num_slots_bet_on()
        else:
            player.print_credits()

            user_input = 3

        # take bets from user's wallet, return in 3x2 array of [slot, bet]
        player.place_bet()

        # Set reference wheel to match spinned wheel so future spins can be properly checked against
        wheel.wheel = wheel.spin_wheel(player)

        # take wheel after spin and bets to get results on the slot user bet on
        result = Result(wheel.wheel, player.placed_bets)

        # calculate results, returns [inSym, midSym, outSym] x3
        result_array = result.resultList()

        # calculate payout based on bets and result symbols
        payout = Payouts(bets, result_array)

        # returns payouts as [credsIn, credsMid, credsOut]
        winnings = payout.calculatePayouts()

        # Place winnings in player's wallet
        for index, winning in enumerate(winnings):
            # Notify player here of any winning bets they had
            winning = int(winning)

            if winning > 0:
                print(
                    "slot " + str(bets[index][0]) + " won " + str(winning) + " credits!"
                )
                player.credits_count += winning

        if player.credits_count >= minBet:
            print("Type 1 to play again, 0 to quit")
            if not Debug:
                user_input = input()
            else:
                user_input = 1

            if user_input == 1:
                continue
            if user_input == 0:
                game_playing = False
        else:
            print("You don't have enough credits to keep playing, game over.")

            sys_exit()

    sys_exit()
