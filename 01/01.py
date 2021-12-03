import time


def part_1(lines):
    count_increase = 0
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i - 1]):
            count_increase += 1
    print("Part 1", count_increase)


def part_2(lines):
    count_increase = 0
    for i in range(3, len(lines)):
        sum_a = int(lines[i]) + int(lines[i - 1]) + int(lines[i - 2])
        sum_b = int(lines[i - 1]) + int(lines[i - 2]) + int(lines[i - 3])
        if sum_a > sum_b:
            count_increase += 1
    print("Part 2", count_increase)


def main():
    with open("input_01.txt", 'r') as in01:
        lines = [line.strip() for line in in01.readlines()]
    s = time.time()
    part_1(lines)
    part_2(lines)
    print(f"Took {time.time() -s:.3f}s")


if __name__ == '__main__':
    main()
