import time


def neighbors(i):
    y = int(i / 10)
    x = i - 10*y
    n = []
    for j in [j for j in [x-1, x, x+1] if 0 <= j < 10]:
        for k in [k for k in [y-1, y, y+1] if 0 <= k < 10]:
            n.append(10*k+j)
    return [j for j in n if j != i]


def evolve(octopuses):
    flashed = [False] * len(octopuses)
    octopuses = [x + 1 for x in octopuses]
    while max(octopuses) > 9:
        for i in range(0, len(octopuses)):
            if flashed[i] or octopuses[i] < 10:
                continue
            flashed[i] = True
            octopuses[i] = 0
            for j in neighbors(i):
                if not flashed[j]:
                    octopuses[j] += 1
    return octopuses, flashed.count(True)


def main():
    with open("input_11.txt", 'r') as in11:
        lines = [line.strip() for line in in11.readlines()]
    s = time.time()

    octopuses = [int(x) for line in lines for x in line]
    count_flash = 0
    for step in range(0, 100):
        octopuses, flashes = evolve(octopuses)
        count_flash += flashes
    print("Part 1:", count_flash)
    big_flashed = False
    real_step = 100
    while not big_flashed:
        real_step += 1
        octopuses, flashes = evolve(octopuses)
        if flashes == 100:
            print("Part 2:", real_step)
            big_flashed = True

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
