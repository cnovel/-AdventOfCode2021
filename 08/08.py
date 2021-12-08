import time


def part_1(lines):
    count = 0
    for line in lines:
        for pattern in line[1]:
            if len(pattern) == 2 or len(pattern) == 3 or len(pattern) == 4 or len(pattern) == 7:
                count += 1

    print("Part 1:", count)


def standard_pattern_to_int(seq):
    if seq == 'abcefg':
        return 0
    if seq == 'cf':
        return 1
    if seq == 'acdeg':
        return 2
    if seq == 'acdfg':
        return 3
    if seq == 'bcdf':
        return 4
    if seq == 'abdfg':
        return 5
    if seq == 'abdefg':
        return 6
    if seq == 'acf':
        return 7
    if seq == 'abcdefg':
        return 8
    if seq == 'abcdfg':
        return 9
    return -1


def line_decoder(line):
    # First, decode the top wire
    one_pattern = sorted([x for x in line[0] if len(x) == 2][0])
    seven_pattern = [x for x in sorted([x for x in line[0] if len(x) == 3][0]) if x not in one_pattern]

    # Select possible remaining segments for 4:
    four_pattern = [x for x in sorted([x for x in line[0] if len(x) == 4][0]) if x not in one_pattern]

    # Select unmatched letters
    unmatched = [x for x in 'abcdefg' if x not in sorted(one_pattern + seven_pattern + four_pattern)]

    # Create all possible dicts
    pos = []
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                possible_d = {seven_pattern[0]: 'a', one_pattern[i]: 'c', one_pattern[(i + 1) % 2]: 'f',
                              four_pattern[j]: 'b', four_pattern[(j + 1) % 2]: 'd', unmatched[k]: 'e',
                              unmatched[(k + 1) % 2]: 'g'}
                pos.append(possible_d)

    # Select the one dict that works
    good_d = None
    for possible_d in pos:
        if good_d is not None:
            continue
        convert_patterns = []
        for pattern in line[0]:
            convert_patterns.append(standard_pattern_to_int(''.join(sorted([possible_d[x] for x in pattern]))))
        if len([x for x in convert_patterns if x < 0]) == 0:
            good_d = possible_d

    # Convert second part to int
    digits = []
    for pattern in line[1]:
        digits.append(str(standard_pattern_to_int(''.join(sorted([good_d[x] for x in pattern])))))
    return int(''.join(digits))


def part_2(lines):
    c = 0
    for line in lines:
        c += line_decoder(line)
    print("Part 2:", c)


def main():
    with open("input_08.txt", 'r') as in08:
        lines = [line.strip() for line in in08.readlines()]
    s = time.time()

    lines = [[line.split(" | ")[0].split(), (line.split(" | ")[1].split())] for line in lines]

    part_1(lines)
    part_2(lines)
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
