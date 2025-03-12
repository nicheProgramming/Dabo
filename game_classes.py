"""Module to store various game necessary classes"""

from abc import ABC, abstractmethod
from random import randrange

from constants import COLORS, MIN_BET, SHAPES


class Player:
    """The player class used to track current credit balance, bumber of remaining spins, etc"""

    def __init__(self):
        self.credits_count = 10000

    def placeBet(self, slot_bet_on: int):
        if self.credits_count >= MIN_BET:
            ...


class Shape(type):
    """Metaclass defining the characteristics of a shape in a given wheel slot"""

    def __new__(mcs, name, bases, attrs):
        attrs["color"] = None
        attrs["shape"] = None
        attrs["_count"] = 0
        attrs["_ring"] = -1

        return super().__new__(mcs, name, bases, attrs)

    @abstractmethod
    def __init__(cls): ...

    @property
    def count(cls):
        """The number of shapes in a given wheel slot"""
        return cls._count

    @count.setter
    def count(cls, value: int):
        cls._count = value

    @property
    def ring(cls):
        """The ring in which the given wheel slot is located (inner, middle, outer)"""
        return cls._ring

    @ring.setter
    def ring(cls, value: int):
        cls._ring = value


class ShapeDs9(metaclass=Shape):
    """Class defining characteristics of the DS9 shape of the dabo wheel slot"""

    def __init__(self):
        self.shape = SHAPES[2]
        self.count = 1


class Wheel(object):
    def __init__(self):
        self.wheel = self.buildWholeWheel()
        self.wheelOffset = [0, 0, 0]
        # Debug variables
        self.referenceWheel = list(self.wheel)

    def buildOneWheel(self, position):
        # The inner wheel doesn't need to account for color, the others do
        if position == 0:
            # Store shape, then number of shapes
            wheel = [
                [SHAPES[4], 3],
                [SHAPES[5], 1],
                [SHAPES[1], 1],
                [SHAPES[6], 3],
                [SHAPES[1], 1],
                [SHAPES[6], 1],
                [SHAPES[4], 2],
                [SHAPES[2], 1],
                [SHAPES[4], 1],
                [SHAPES[4], 3],
                [SHAPES[1], 3],
                [SHAPES[4], 2],
                [SHAPES[0], 1],
                [SHAPES[1], 1],
                [SHAPES[4], 3],
                [SHAPES[6], 2],
                [SHAPES[6], 1],
                [SHAPES[0], 1],
                [SHAPES[1], 3],
                [SHAPES[4], 1],
                [SHAPES[2], 1],
                [SHAPES[6], 2],
                [SHAPES[0], 1],
                [SHAPES[1], 2],
                [SHAPES[6], 1],
                [SHAPES[1], 3],
                [SHAPES[3], 1],
                [SHAPES[6], 3],
                [SHAPES[1], 2],
                [SHAPES[6], 2],
                [SHAPES[4], 1],
                [SHAPES[2], 1],
                [SHAPES[6], 3],
                [SHAPES[4], 2],
                [SHAPES[0], 1],
                [SHAPES[1], 2],
            ]
        # Store shape, number of shapes, then color
        elif position == 1:
            wheel = [
                [SHAPES[6], 1, COLORS[0]],
                [SHAPES[1], 3, COLORS[2]],
                [SHAPES[3], 1, None],
                [SHAPES[6], 3, COLORS[1]],
                [SHAPES[1], 2, COLORS[0]],
                [SHAPES[6], 2, COLORS[1]],
                [SHAPES[4], 1, COLORS[2]],
                [SHAPES[2], 1, None],
                [SHAPES[6], 3, COLORS[0]],
                [SHAPES[4], 2, COLORS[1]],
                [SHAPES[0], 1, None],
                [SHAPES[1], 2, COLORS[2]],
                [SHAPES[4], 3, COLORS[0]],
                [SHAPES[5], 1, None],
                [SHAPES[1], 1, COLORS[1]],
                [SHAPES[6], 3, COLORS[2]],
                [SHAPES[1], 1, COLORS[0]],
                [SHAPES[6], 1, COLORS[1]],
                [SHAPES[4], 2, COLORS[2]],
                [SHAPES[2], 1, None],
                [SHAPES[4], 1, COLORS[0]],
                [SHAPES[4], 3, COLORS[2]],
                [SHAPES[1], 3, COLORS[1]],
                [SHAPES[4], 2, COLORS[0]],
                [SHAPES[0], 1, None],
                [SHAPES[1], 1, COLORS[2]],
                [SHAPES[4], 3, COLORS[1]],
                [SHAPES[6], 2, COLORS[0]],
                [SHAPES[6], 1, COLORS[2]],
                [SHAPES[5], 1, None],
                [SHAPES[1], 3, COLORS[0]],
                [SHAPES[4], 1, COLORS[1]],
                [SHAPES[2], 1, None],
                [SHAPES[6], 2, COLORS[2]],
                [SHAPES[0], 1, None],
                [SHAPES[1], 2, COLORS[1]],
            ]
        elif position == 2:
            # Store shape, number of shapes, then color
            wheel = [
                [SHAPES[0], 1, None],
                [SHAPES[1], 2, COLORS[1]],
                [SHAPES[6], 1, COLORS[0]],
                [SHAPES[1], 3, COLORS[2]],
                [SHAPES[3], 1, None],
                [SHAPES[6], 3, COLORS[1]],
                [SHAPES[1], 2, COLORS[0]],
                [SHAPES[6], 2, COLORS[1]],
                [SHAPES[4], 1, COLORS[2]],
                [SHAPES[2], 1, None],
                [SHAPES[6], 3, COLORS[0]],
                [SHAPES[4], 2, COLORS[1]],
                [SHAPES[0], 1, None],
                [SHAPES[1], 2, COLORS[2]],
                [SHAPES[4], 3, COLORS[0]],
                [SHAPES[5], 1, None],
                [SHAPES[1], 1, COLORS[1]],
                [SHAPES[6], 3, COLORS[2]],
                [SHAPES[1], 1, COLORS[0]],
                [SHAPES[6], 1, COLORS[1]],
                [SHAPES[4], 2, COLORS[2]],
                [SHAPES[2], 1, None],
                [SHAPES[4], 1, COLORS[0]],
                [SHAPES[4], 3, COLORS[2]],
                [SHAPES[1], 3, COLORS[1]],
                [SHAPES[4], 2, COLORS[0]],
                [SHAPES[0], 1, None],
                [SHAPES[1], 1, COLORS[2]],
                [SHAPES[4], 3, COLORS[1]],
                [SHAPES[6], 2, COLORS[0]],
                [SHAPES[6], 1, COLORS[2]],
                [SHAPES[5], 1, None],
                [SHAPES[1], 3, COLORS[0]],
                [SHAPES[4], 1, COLORS[1]],
                [SHAPES[2], 1, None],
                [SHAPES[6], 2, COLORS[2]],
            ]
        return wheel

    def buildWholeWheel(self):
        result = [[], [], []]

        result[0] = self.buildOneWheel(0)
        result[1] = self.buildOneWheel(1)
        result[2] = self.buildOneWheel(2)

        return result

    def spinWheel(self, player: Player):
        self.wheelOffset = [
            randrange(0, 35),
            randrange(0, 35),
            randrange(0, 35),
        ]
        index = 0

        while self.wheelOffset[0] > 0:
            # Put first item in array at the end of the array
            self.wheel[0] = self.wheel[0][1:] + [self.wheel[0][0]]
            self.wheelOffset[0] -= 1

            # make sure last item in wheel matches item in reference wheel at offset iteration index (index of how many times offset has been applied)
            if self.wheel[0][-1] != self.referenceWheel[0][index]:
                print("!!!wheel not spinning properly!!!")
                print("Last item in self.wheel[0] is " + str(self.wheel[0][-1]))
                print("expected: " + str(self.referenceWheel[0][index]))
                exit()

            index += 1

        # must be reset after each wheel spin
        index = 0

        while self.wheelOffset[1] > 0:
            # Put last item of array in first place
            # This is reversed on purpose, this wheel spins counter clockwise, unlike the other two wheels
            self.wheel[1] = [self.wheel[1][-1]] + self.wheel[1][:-1]
            self.wheelOffset[1] -= 1

            # make sure first item in wheel matches item in reference wheel at reverse offset iteration index (index of how many times offset has been applied)
            if self.wheel[1][0] != self.referenceWheel[1][-index - 1]:
                print("!!!wheel not spinning properly!!!")
                print("First item in self.wheel[1] is " + str(self.wheel[1][0]))
                print("expected: " + str(self.referenceWheel[1][-index - 1]))
                exit()

            index += 1

            # print("First item in self.wheel[1] is " + str(self.wheel[1][0]))
            # # Print the expected wheel item to ensure array is moving as anticipated
            # print ("expected: " + self.referenceWheel[1][(0+index)])

        # must be reset after each wheel spin
        index = 0

        while self.wheelOffset[2] > 0:
            # Put first item in array at the end of the array
            self.wheel[2] = self.wheel[2][1:] + [self.wheel[2][0]]
            self.wheelOffset[2] -= 1

            # make sure last item in wheel matches item in reference wheel at offset iteration index (index of how many times offset has been applied)
            if self.wheel[2][-1] != self.referenceWheel[2][index]:
                print("!!!wheel not spinning properly!!!")
                print("Last item in self.wheel[2] is " + str(self.wheel[2][-1]))
                print("expected: " + str(self.referenceWheel[2][(index)]))
                exit()

            index += 1

        # Set ref wheel to VALUE, no OBJECT of wheel after spin for continuitiy
        self.referenceWheel = list(self.wheel)

        player.numOfSpins += 1

        return self.wheel
