"""Module to store various unchanging game values"""

MAX_BET = 1000  # credits
MIN_BET = 10
MAX_SLOTS_PER_SPIN = 3  # num of slots you can bet on per spin
SHAPES = ("black hole", "circle", "ds9", "quark", "square", "swirl", "triangle")
COLORS = ("red", "green", "blue")
# 0 for the inner, colorless ring, 1 for the middle ring, 2 for the outer ring
RINGS = (0, 1, 2)
STATIC_FILES = "game_data/static_files/"
DYNAMIC_FILES = "game_data/dynamic_files/"
BETTABLE_SLOTS = [
    0,
    1,
    2,
    3,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    31,
    32,
    33,
    34,
]
