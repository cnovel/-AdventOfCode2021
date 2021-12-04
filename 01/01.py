import time


def part_1(values):
    count_increase = 0
    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            count_increase += 1
    print("Part 1", count_increase)


def part_2(values):
    count_increase = 0
    for i in range(3, len(values)):
        sum_a = values[i] + values[i - 1] + values[i - 2]
        sum_b = values[i - 1] + values[i - 2] + values[i - 3]
        if sum_a > sum_b:
            count_increase += 1
    print("Part 2", count_increase)


def main():
    with open("input_01.txt", 'r') as in01:
        values = [int(line.strip()) for line in in01.readlines()]
    s = time.time()
    part_1(values)
    part_2(values)
    print(f"Took {time.time() -s:.3f}s")


if __name__ == '__main__':
    main()
