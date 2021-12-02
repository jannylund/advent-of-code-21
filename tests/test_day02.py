from day02 import *

raw_course = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

course = [parse_cmd(cmd) for cmd in raw_course.splitlines()]


def test_day02_part1():
    # (horizontal, depth)
    assert navigate(course[:1]) == (5, 0)
    assert navigate(course[:2]) == (5, 5)
    assert navigate(course[:3]) == (13, 5)
    assert navigate(course[:4]) == (13, 2)
    assert navigate(course[:5]) == (13, 10)
    assert navigate(course[:6]) == (15, 10)

    horizontal, depth = navigate(course)
    assert horizontal * depth == 150


def test_day02_part1():
    # (horizontal, depth, aim)
    assert navigate_aim(course[:1]) == (5, 0, 0)
    assert navigate_aim(course[:2]) == (5, 0, 5)
    assert navigate_aim(course[:3]) == (13, 40, 5)
    assert navigate_aim(course[:4]) == (13, 40, 2)
    assert navigate_aim(course[:5]) == (13, 40, 10)
    assert navigate_aim(course[:6]) == (15, 60, 10)

    horizontal, depth, aim = navigate_aim(course)
    assert horizontal * depth == 900
