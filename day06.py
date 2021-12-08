from utils.time import get_time, start_timer


def simulate(fish, days):
    fishcount = {}
    for i in range(len(fish)):
        if fish[i] not in fishcount:
            fishcount[fish[i]] = 1
        else:
            fishcount[fish[i]] += 1

    for i in range(days):
        newfish = {}
        for src in fishcount.keys():
            if src == 0:
                target = 6
                newfish[8] = fishcount[0]
            else:
                target = int(src) - 1

            if not target in newfish:
                newfish[target] = fishcount[src]
            else:
                newfish[target] += fishcount[src]
        fishcount = newfish
    return sum(fishcount.values())


if __name__ == "__main__":
    with open("input/day06.txt") as f:
        fish = f.read().split(",")

    start = start_timer()
    print("result day 06 part 1: fish_count={} in {} ms".format(simulate(fish, 80), get_time(start)))

    start = start_timer()
    print("result day 06 part 2: fish_count={} in {} ms".format(simulate(fish, 256), get_time(start)))
