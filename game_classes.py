"""Module to store various game necessary classes"""

from dataclasses import dataclass
from json import loads
from random import randrange
from sys import exit as sys_exit
from typing import Optional

from constants import (
    BETTABLE_SLOTS,
    COLORS,
    MAX_BET,
    MAX_SLOTS_PER_SPIN,
    MIN_BET,
    RINGS,
    SHAPES,
    STATIC_FILES,
)


@dataclass
class Bet:
    slot: int
    bet: int


class Color:
    def __init__(self, color: int):
        self.color: int = color

    def __repr__(self):
        return self.translate_color()

    def translate_color(self):
        """Translate the color value to a string using the COLORS constant"""
        if 0 <= self.color < len(COLORS):
            return COLORS[self.color]
        raise ValueError(f"Invalid color value: {self.color}")


class Glyph:
    """Class defining the characteristics of a shape in a given wheel slot"""

    def __init__(self, shape: int, count: int, color: Optional[int], wheel: int):
        self.shape: Shape = Shape(shape)
        self._count: int = count
        self.color: Optional[Color] = Color(color) if color is not None else None
        self._ring: Ring = wheel

    def __repr__(self):
        return f"{self._ring} Glyph {self.shape} {self.color if self.color else ''} {self._count}"

    @property
    def count(self):
        """The number of shapes in a given wheel slot"""
        return self._count

    @count.setter
    def count(self, value: int):
        self._count = value

    @property
    def ring(self):
        """The ring in which the given wheel slot is located (inner, middle, outer)"""
        return self._ring

    @ring.setter
    def ring(self, value: int):
        self._ring = value


class Player:
    """The player class used to track current credit balance, number of remaining spins, etc"""

    def __init__(self):
        self.credits_count: int = 10000
        # store the number of slots bet on from user input
        self.num_slots_bet_on: int = 0
        self.placed_bets: list[Bet] = []

    def place_bet(self):
        bets_remaining = self.num_slots_bet_on
        readable_slots = ", ".join(str(x + 1) for x in BETTABLE_SLOTS)

        # TODO: Add logic here to ensure enough money in wallet for all bets
        while bets_remaining > 0:
            if self.credits_count < MIN_BET:
                print("You don't have enough credits to place any more bets")

                bets_remaining = 0

                return

            selected_slot = int(
                self.get_user_input(f"Enter slot to bet on {readable_slots}): ")
            )
            bet_range: str = f"({MIN_BET} - {MAX_BET})"

            if selected_slot - 1 not in BETTABLE_SLOTS:
                print("Invalid slot, try again")

                continue

            if len(self.placed_bets) > 0 and selected_slot in [
                bet.slot for bet in self.placed_bets
            ]:
                print("You already placed a bet on that slot, try again")

                continue

            bet_amount = int(
                self.get_user_input(f"Enter bet for slot {selected_slot} {bet_range}: ")
            )

            if not self.__valid_bet(bet_amount):
                continue

            self.credits_count -= bet_amount

            self.placed_bets.append(Bet(selected_slot - 1, bet_amount))

            bets_remaining -= 1

            print(f"Bet of {bet_amount:,} placed on slot {self.placed_bets[-1].slot}")

    def __valid_bet(self, bet_amount: int) -> bool:
        """Determine if the amount entered by user for bet is valid

        Args:
            bet_amount (int): Integer value of bet amount

        Returns:
            bool: True if in valid range, False elsewise
        """
        if bet_amount < MIN_BET:
            print(f"Bet must be no less than {MIN_BET} credits per slot")

            return False
        if bet_amount > MAX_BET:
            print(f"Bet may be no more than {MAX_BET} credits per slot")

            return False

        if bet_amount > self.credits_count:
            print(
                f"You only have {self.credits_count:,} credits remaining, bet cannot be fulfilled"
            )

            return False

        return True

    def get_user_input(self, prompt: str) -> str:
        """Get user input with a text prompt

        Args:
            prompt (str): _description_

        Returns:
            str: _description_
        """
        print(prompt)

        return input()

    def get_num_slots_bet_on(self):
        """Determine the number of slots the player wants to bet on this round"""
        num_slots_bet_on = int(
            self.get_user_input("Enter number of slots to bet on (0-3): ")
        )

        if num_slots_bet_on == 0:
            sys_exit()
        elif num_slots_bet_on > MAX_SLOTS_PER_SPIN:
            print("Too many slots bet on, try again")
        else:
            self.num_slots_bet_on = num_slots_bet_on

    def print_credits(self):
        """Print the number of credits the player has remaining in their wallet"""
        print(f"You have {self.credits_count:,} credits remaining.")


class Ring:
    """Class defining the characteristics of a ring in a given wheel slot"""

    def __init__(self, ring: int):
        self.ring: int = ring

    def __repr__(self):
        return self.translate_ring()

    def translate_ring(self):
        """Translate the ring value to a string using the RINGS constant"""
        if 0 <= self.ring < len(RINGS):
            return RINGS[self.ring]
        raise ValueError(f"Invalid ring value: {self.ring}")

    def wheel_dictionary(self, wheel_str: Optional[int] = None):
        wheel_translator = {
            "inner_wheel": 0,
            "middle_wheel": 1,
            "outer_wheel": 2,
        }

        if wheel_str is None:
            return wheel_translator


class Shape:
    def __init__(self, shape: int):
        self.shape: int = shape

    def __repr__(self):
        return self.translate_shape()

    def translate_shape(self):
        """Translate the shape value to a string using the SHAPES constant"""
        if 0 <= self.shape < len(SHAPES):
            return SHAPES[self.shape]
        raise ValueError(f"Invalid shape value: {self.shape}")


class Wheel(object):
    def __init__(self):
        # self.wheel = self.buildWholeWheel()
        with open(
            STATIC_FILES + "color_index.json", "r", encoding="utf-8"
        ) as colors_file:
            self.colors_index: list[str] = loads(colors_file.read())["colors"]
        with open(
            STATIC_FILES + "shape_index.json", "r", encoding="utf-8"
        ) as shapes_file:
            self.shapes_index: list[str] = loads(shapes_file.read())["shapes"]
        self.wheel: list[list] = [[], [], []]
        self.load_wheel()
        self.wheel_offset = [0, 0, 0]
        # Debug variables
        self.reference_wheel = list(self.wheel)

    def load_wheel(self):

        with open(
            STATIC_FILES + "default_wheel.json", "r", encoding="utf-8"
        ) as wheel_file:
            raw_wheel_data: dict[str, list[dict[str, int]]] = loads(wheel_file.read())

            for wheel, slots in raw_wheel_data.items():
                if "wheel" in wheel:
                    self.parse_slots(wheel, slots)

            self.wheel = self.reference_wheel = list(raw_wheel_data)

    def parse_slots(self, wheel: str, slots: list[dict[str, int]]):
        wheel_translator = {
            "inner_wheel": 0,
            "middle_wheel": 1,
            "outer_wheel": 2,
        }
        wheel_index = wheel_translator[wheel]

        for slot in slots:
            new_shape = Glyph(slot["shape"], slot["count"], slot["color"], wheel_index)

            self.wheel[wheel_index].append(new_shape)

    def spin_wheel(self, player: Player):
        lower_end = BETTABLE_SLOTS[0]
        upper_end = BETTABLE_SLOTS[-1]

        self.wheel_offset = [
            randrange(lower_end, upper_end),
            randrange(lower_end, upper_end),
            randrange(lower_end, upper_end),
        ]
        index = 0

        for index, offset in enumerate(self.wheel_offset):
            while offset > 0:
                # TODO: Check if 0 index or 1 index.
                if index in (0, 2):
                    ...
                elif index == 1:
                    ...
                else:
                    raise ValueError("Invalid index for wheel offset")

        while self.wheel_offset[0] > 0:
            # Put first item in array at the end of the array
            self.wheel[0] = self.wheel[0][1:] + [self.wheel[0][0]]
            self.wheel_offset[0] -= 1

            # make sure last item in wheel matches item in reference wheel at offset iteration index (index of how many times offset has been applied)
            if self.wheel[0][-1] != self.reference_wheel[0][index]:
                print("!!!wheel not spinning properly!!!")
                print("Last item in self.wheel[0] is " + str(self.wheel[0][-1]))
                print("expected: " + str(self.reference_wheel[0][index]))
                sys_exit()

            index += 1

        # must be reset after each wheel spin
        index = 0

        while self.wheel_offset[1] > 0:
            # Put last item of array in first place
            # This is reversed on purpose, this wheel spins counter clockwise, unlike the other two wheels
            self.wheel[1] = [self.wheel[1][-1]] + self.wheel[1][:-1]
            self.wheel_offset[1] -= 1

            # make sure first item in wheel matches item in reference wheel at reverse offset iteration index (index of how many times offset has been applied)
            if self.wheel[1][0] != self.reference_wheel[1][-index - 1]:
                print("!!!wheel not spinning properly!!!")
                print("First item in self.wheel[1] is " + str(self.wheel[1][0]))
                print("expected: " + str(self.reference_wheel[1][-index - 1]))
                sys_exit()

            index += 1

            # print("First item in self.wheel[1] is " + str(self.wheel[1][0]))
            # # Print the expected wheel item to ensure array is moving as anticipated
            # print ("expected: " + self.reference_wheel[1][(0+index)])

        # must be reset after each wheel spin
        index = 0

        while self.wheel_offset[2] > 0:
            # Put first item in array at the end of the array
            self.wheel[2] = self.wheel[2][1:] + [self.wheel[2][0]]
            self.wheel_offset[2] -= 1

            # make sure last item in wheel matches item in reference wheel at offset iteration index (index of how many times offset has been applied)
            if self.wheel[2][-1] != self.reference_wheel[2][index]:
                print("!!!wheel not spinning properly!!!")
                print("Last item in self.wheel[2] is " + str(self.wheel[2][-1]))
                print("expected: " + str(self.reference_wheel[2][(index)]))
                sys_exit()

            index += 1

        # Set ref wheel to VALUE, no OBJECT of wheel after spin for continuitiy
        self.reference_wheel = list(self.wheel)

        player.numOfSpins += 1

        return self.wheel
