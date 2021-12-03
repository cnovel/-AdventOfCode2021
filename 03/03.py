import time


def filter_bits(number_to_filter, pos):
    c = 0
    threshold = len(number_to_filter) / 2
    for n in number_to_filter:
        if n[pos] == '1':
            c += 1

    if c >= threshold:
        most_common = [n for n in number_to_filter if n[pos] == '1']
        least_common = [n for n in number_to_filter if n[pos] == '0']
    else:
        most_common = [n for n in number_to_filter if n[pos] == '0']
        least_common = [n for n in number_to_filter if n[pos] == '1']
    return most_common, least_common


def part_1(lines):
    # Part 1
    count_1 = [0 for x in lines[0]]
    for line in lines:
        for i in range(0, len(line)):
            if line[i] == '1':
                count_1[i] += 1

    gamma = ''
    epsilon = ''
    threshold = len(lines) / 2
    for c in count_1:
        if c > threshold:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma_i = int(gamma, 2)
    epsilon_i = int(epsilon, 2)

    print("Power:", gamma_i * epsilon_i)


def part_2(lines):
    oxygen = lines
    co2 = lines
    pos = 0
    while len(oxygen) > 1 and pos < len(lines[0]):
        oxygen, _ = filter_bits(oxygen, pos)
        pos += 1
    ox = int(oxygen[0], 2)

    pos = 0
    while len(co2) > 1 and pos < len(lines[0]):
        _, co2 = filter_bits(co2, pos)
        pos += 1
    c = int(co2[0], 2)
    print("Support:", c*ox)


def main():
    with open("input_03.txt", 'r') as in03:
        lines = [line.strip() for line in in03.readlines()]
    s = time.time()
    part_1(lines)
    part_2(lines)
    print(f"Took {time.time() -s:.3f}s")


if __name__ == '__main__':
    main()
