import time


def parse_line(line):
    snail = []
    level = 0
    for x in line:
        if x == '[':
            level += 1
        elif x == ']':
            level -= 1
        elif x == ',':
            continue
        else:
            snail.append([int(x), level])
    return snail


def add_snail(snail_a, snail_b):
    new_snail = []
    for x in snail_a:
        new_snail.append([x[0], x[1]+1])
    for x in snail_b:
        new_snail.append([x[0], x[1]+1])
    return new_snail


def magnitude(snail):
    # We'll try to reduce from level 4 to level 0
    step = 4
    while len(snail) > 1 and step != 0:
        new_snail = []
        skip = False
        for i in range(0, len(snail)):
            if skip:
                skip = False
                continue

            if snail[i][1] == step:
                mag = 3*snail[i][0] + 2*snail[i+1][0]
                skip = True
                new_snail.append([mag, step-1])
                continue

            new_snail.append(snail[i])
        snail = new_snail
        step -= 1
    return snail[0][0]


def process_snail(snail):
    change = True
    while change:
        new_snail = []
        change = False
        skip = False
        for i in range(0, len(snail)):
            if skip:
                skip = False
                continue

            if change:
                new_snail.append(snail[i])
                continue

            if snail[i][1] > 4:  # Explode
                if len(new_snail) > 0:
                    new_snail[-1][0] += snail[i][0]
                if i+2 < len(snail):
                    snail[i+2][0] += snail[i+1][0]
                new_snail.append([0, snail[i][1]-1])
                skip = True
                change = True
                continue

            new_snail.append(snail[i])
        snail = new_snail
        if change:
            continue

        new_snail = []
        for i in range(0, len(snail)):
            if skip:
                skip = False
                continue

            if change:
                new_snail.append(snail[i])
                continue

            if snail[i][0] > 9:  # Split
                i_left = int(snail[i][0]/2)
                i_right = int(snail[i][0]/2 + 0.5)
                new_snail.append([i_left, snail[i][1] + 1])
                new_snail.append([i_right, snail[i][1] + 1])
                change = True
                continue

            new_snail.append(snail[i])

        snail = new_snail
    return snail


def main():
    with open("input_18.txt", 'r') as in18:
        lines = [line.strip() for line in in18.readlines()]
    s = time.time()

    snails = [parse_line(line) for line in lines]
    snail = process_snail(snails[0])
    for i in range(1, len(snails)):
        snail = add_snail(snail, snails[i])
        snail = process_snail(snail)

    print("Part 1:", magnitude(snail))

    mag_max = 0
    for i in range(0, len(snails)):
        for j in range(i+1, len(snails)):
            mag_a = magnitude(process_snail(add_snail(snails[i], snails[j])))
            mag_b = magnitude(process_snail(add_snail(snails[j], snails[i])))
            mag_max = max(mag_max, mag_a)
            mag_max = max(mag_max, mag_b)
    print("Part 2:", mag_max)

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
