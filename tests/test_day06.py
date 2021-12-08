from day06 import *

fish = "3,4,3,1,2".split(",")


def test_day06_part1():
    assert len(fish) == 5
    assert simulate(fish, 18) == 26
    assert simulate(fish, 80) == 5934