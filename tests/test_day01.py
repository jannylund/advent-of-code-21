from day01 import *

depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_day01_part1():
    assert calc_increases(depths) == 7


def test_day01_part2():
    assert calc_increases(sliding_window(depths)) == 5
