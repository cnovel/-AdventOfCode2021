import time


def part_1(lines):
    x = 0
    y = 0
    for line in lines:
        cmd = line.split(' ')[0]
        value = int(line.split(' ')[1])
        if cmd == "forward":
            x += value
        elif cmd == "down":
            y += value
        else:
            y -= value

    print("Product 1:", x * y)


def part_2(lines):
    x = 0
    y = 0
    aim = 0

    for line in lines:
        cmd = line.split(' ')[0]
        value = int(line.split(' ')[1])
        if cmd == "forward":
            x += value
            y += aim * value
        elif cmd == "down":
            aim += value
        else:
            aim -= value

    print("Product 2:", x * y)


def main():
    with open("input_02.txt", 'r') as in02:
        lines = [line.strip() for line in in02.readlines()]

    s = time.time()
    part_1(lines)
    part_2(lines)
    print(f"Took {time.time() -s:.3f}s")


if __name__ == '__main__':
    main()
