import time


def part_1(lines):
    w = len(lines[0])
    h = len(lines)
    risk_levels = 0
    for i in range(0, w):
        for j in range(0, h):
            p = lines[j][i]
            if j - 1 >= 0 and lines[j - 1][i] <= p:
                continue
            if j + 1 < h and lines[j + 1][i] <= p:
                continue
            if i - 1 >= 0 and lines[j][i - 1] <= p:
                continue
            if i + 1 < w and lines[j][i + 1] <= p:
                continue
            risk_levels += p + 1

    print("Part 1:", risk_levels)


def part_2(lines):
    w = len(lines[0])
    h = len(lines)
    grow_map = [[1 if x != 9 else 0 for x in line] for line in lines]
    basin_sizes = []
    for i in range(0, w):
        for j in range(0, h):
            p = grow_map[j][i]
            if p == 0:
                continue
            queue = [(j, i)]
            basin_size = 0
            while len(queue) != 0:
                y, x = queue.pop(0)
                if grow_map[y][x] == 0:
                    continue
                grow_map[y][x] = 0
                basin_size += 1
                if y-1 >= 0 and grow_map[y-1][x] != 0:
                    queue.append((y-1, x))
                if y+1 < h and grow_map[y+1][x] != 0:
                    queue.append((y+1, x))
                if x-1 >= 0 and grow_map[y][x-1] != 0:
                    queue.append((y, x-1))
                if x+1 < w and grow_map[y][x+1] != 0:
                    queue.append((y, x+1))
            basin_sizes.append(basin_size)

    basin_sizes.sort()
    print("Part 2:", basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])


def main():
    with open("input_09.txt", 'r') as in09:
        lines = [line.strip() for line in in09.readlines()]
    s = time.time()

    lines = [[int(x) for x in line] for line in lines]
    part_1(lines)
    part_2(lines)

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
