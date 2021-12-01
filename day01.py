from utils.time import get_time, start_timer


def calc_increases(arr):
    increases = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            increases += 1
    return increases


def sliding_window(arr, size=3):
    ret_arr = []
    for i in range(len(arr) - (size - 1)):
        ret_arr.append(sum(arr[i : i + size]))
    return ret_arr


if __name__ == "__main__":
    with open("input/day01.txt") as f:
        depths = [int(d) for d in f.read().splitlines()]

    start = start_timer()
    print("result day 01 part 1: increases={} in {} ms".format(calc_increases(depths), get_time(start)))

    start = start_timer()
    slide_arr = sliding_window(depths)
    print("result day 01 part 2: sliding_increases={} in {} ms".format(calc_increases(slide_arr), get_time(start)))
