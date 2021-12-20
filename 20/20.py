import time


def zone_to_value(zone, rule):
    s = ''.join('0' if x == '.' else '1' for x in zone)
    return rule[int(s, 2)]


def get_min_max(img: dict):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for key in img.keys():
        min_x = min(min_x, key[0])
        max_x = max(max_x, key[0])
        min_y = min(min_y, key[1])
        max_y = max(max_y, key[1])
    return min_x, max_x, min_y, max_y


def get_nb_lit(img):
    lit = 0
    for v in img.values():
        lit += 1 if v == '#' else 0
    return lit


def main():
    with open("input_20.txt", 'r') as in20:
        lines = [line.strip() for line in in20.readlines()]
    s = time.time()

    rule = lines[0]
    img = {}
    for i in range(2, len(lines)):
        for j in range(0, len(lines[2])):
            img[(j, i-2)] = lines[i][j]

    default = '.'
    for step in range(0, 50):
        new_img = {}
        min_x, max_x, min_y, max_y = get_min_max(img)
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                zone = []
                for Y in [y-1, y, y+1]:
                    for X in [x-1, x, x+1]:
                        zone.append(img.get((X, Y), default))
                new_img[(x, y)] = zone_to_value(zone, rule)
        img = new_img
        default = zone_to_value([default]*9, rule)
        if step == 1:
            print("Part 1:", get_nb_lit(img))
        if step == 49:
            print("Part 2:", get_nb_lit(img))

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
