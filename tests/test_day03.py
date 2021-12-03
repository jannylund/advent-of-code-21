from day03 import *

diagnostic_report = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()


def test_day03_part1():
    assert most_common_bit(diagnostic_report, position=0) == 1
    assert most_common_bit(diagnostic_report, position=1) == 0
    assert most_common_bit(diagnostic_report, position=2) == 1
    assert most_common_bit(diagnostic_report, position=3) == 1
    assert most_common_bit(diagnostic_report, position=4) == 0

    assert get_gamma(diagnostic_report) == 22
    assert get_epsilon(diagnostic_report) == 9

    power_consumption = get_gamma(diagnostic_report) * get_epsilon(diagnostic_report)
    assert power_consumption == 198


def test_day03_part2():
    assert get_oxygen_generator_rating(diagnostic_report) == 23
    assert get_co2_scrubber_rating(diagnostic_report) == 10

    assert life_support_rating(diagnostic_report) == 230
