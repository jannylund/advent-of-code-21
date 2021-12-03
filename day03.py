from utils.time import get_time, start_timer


def most_common_bit(arr, position):
    ones = 0
    for item in arr:
        if item[position] == "1":
            ones += 1

    zeroes = len(arr) - ones

    if ones >= zeroes:
        return 1
    else:
        return 0


def least_common_bit(arr, position):
    if len(arr) == 1:
        return int(arr[0][position])

    if most_common_bit(arr, position) == 1:
        return 0
    return 1


def get_gamma(arr):
    gamma = ""
    for i in range(len(arr[0])):
        gamma += str(most_common_bit(arr, i))
    return _bin_dec(gamma)


def get_epsilon(arr):
    epsilon = ""
    for i in range(len(arr[0])):
        epsilon += str(least_common_bit(arr, i))
    return _bin_dec(epsilon)


def _bin_dec(binary):
    return int(binary, 2)


def filter_pos(arr, pos, val):
    ret = []
    for item in arr:
        if item[pos] == str(val):
            ret.append(item)
    return ret


def get_oxygen_generator_rating(arr):
    loops = len(arr[0])
    for i in range(loops):
        val = most_common_bit(arr, i)
        arr = filter_pos(arr, i, val)
    return _bin_dec(arr[0])


def get_co2_scrubber_rating(arr):
    loops = len(arr[0])
    for i in range(loops):
        val = least_common_bit(arr, i)
        arr = filter_pos(arr, i, val)
    return _bin_dec(arr[0])


def life_support_rating(arr):
    return get_oxygen_generator_rating(arr) * get_co2_scrubber_rating(arr)


if __name__ == "__main__":
    with open("input/day03.txt") as f:
        diagnostic_report = f.read().splitlines()

    start = start_timer()
    power_consumption = get_gamma(diagnostic_report) * get_epsilon(diagnostic_report)
    print("result day 03 part 1: power_consumption={} in {} ms".format(power_consumption, get_time(start)))

    start = start_timer()
    print("result day 03 part 2: life_support_rating={} in {} ms".format(life_support_rating(diagnostic_report), get_time(start)))
