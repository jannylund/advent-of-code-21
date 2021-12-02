from utils.time import get_time, start_timer


def parse_cmd(cmd):
    op, unit = cmd.split(" ")
    return op, int(unit)


def navigate(commands, pos=(0, 0)):
    horizontal, depth = pos
    for op, unit in commands:
        if op == "forward":
            horizontal = horizontal + unit
        elif op == "down":
            depth = depth + unit
        elif op == "up":
            depth = depth - unit
    return horizontal, depth


def navigate_aim(commands, pos=(0, 0, 0)):
    horizontal, depth, aim = pos
    for op, unit in commands:
        if op == "forward":
            depth = depth + aim * unit
            horizontal = horizontal + unit
        elif op == "down":
            aim = aim + unit
        elif op == "up":
            aim = aim - unit
    return horizontal, depth, aim


if __name__ == "__main__":
    with open("input/day02.txt") as f:
        course = [parse_cmd(cmd) for cmd in f.read().splitlines()]

    start = start_timer()
    horizontal, depth = navigate(course)
    print("result day 02 part 1: position={}, result={} in {} ms".format((horizontal, depth), horizontal * depth, get_time(start)))

    start = start_timer()
    horizontal, depth, aim = navigate_aim(course)
    print("result day 02 part 2: position={}, result={} in {} ms".format((horizontal, depth, aim), horizontal * depth, get_time(start)))
