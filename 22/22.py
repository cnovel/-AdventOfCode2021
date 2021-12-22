import time


def part_1(lines):
    count = set()
    for line in lines:
        min_x = max(-50, line[1][0])
        min_y = max(-50, line[1][2])
        min_z = max(-50, line[1][4])
        max_x = min(50, line[1][1])
        max_y = min(50, line[1][3])
        max_z = min(50, line[1][5])
        if min_x > max_x or min_y > max_y or min_z > max_z:
            continue  # Invalid interval

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    if line[0] == 'on':
                        count.add((x, y, z))
                    elif (x, y, z) in count:
                        count.remove((x, y, z))

    print("Part 1:", len(count))


def main():
    with open("input_22.txt", 'r') as in22:
        lines = [line.strip() for line in in22.readlines()]
    s = time.time()

    lines = [line.split(" ") for line in lines]
    lines = [(line[0], line[1].split(",")) for line in lines]
    new_lines = []
    for line in lines:
        coords = line[1]
        new_coords = []
        for coord in coords:
            c = coord[2:].split("..")
            for m in c:
                new_coords.append(int(m))
        new_lines.append((line[0], new_coords))
    lines = new_lines

    part_1(lines)
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
