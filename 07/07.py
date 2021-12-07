import time
from collections import Counter


def part_1(crab_pos):
    fuel_burn = -1
    best_pos = -1
    for pos in range(crab_pos[0], crab_pos[-1] + 1):
        fuel_burn_pos = 0
        for crab in crab_pos:
            fuel_burn_pos += abs(crab - pos)
        if fuel_burn < 0:
            fuel_burn = fuel_burn_pos
            best_pos = pos
        if fuel_burn_pos < fuel_burn:
            fuel_burn = fuel_burn_pos
            best_pos = pos
    print("Part 1 - Best position:", best_pos)
    print("Part 1 - Fuel burn:", fuel_burn)


def part_2(crab_pos):
    fuel_burn = -1
    best_pos = -1
    for pos in range(crab_pos[0], crab_pos[-1] + 1):
        fuel_burn_pos = 0
        for crab in crab_pos:
            dist = abs(crab - pos)
            fuel_burn_pos += dist * (dist+1) / 2  # Sum 1 to n
            if 0 < fuel_burn < fuel_burn_pos:
                break
        if fuel_burn < 0:
            fuel_burn = fuel_burn_pos
            best_pos = pos
        if fuel_burn_pos < fuel_burn:
            fuel_burn = fuel_burn_pos
            best_pos = pos
    print("Part 2 - Best position:", best_pos)
    print("Part 2 - Fuel burn:", int(fuel_burn))


def main():
    with open("input_07.txt", 'r') as in07:
        lines = [line.strip() for line in in07.readlines()]
    s = time.time()
    crab_pos = [int(x) for x in lines[0].split(",")]
    crab_pos.sort()
    part_1(crab_pos)
    part_2(crab_pos)
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
