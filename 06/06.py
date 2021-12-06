import time
from collections import Counter


def main():
    with open("input_06.txt", 'r') as in05:
        lines = [line.strip() for line in in05.readlines()]
    s = time.time()

    state = [int(x) for x in lines[0].split(",")]
    counter = Counter(state)
    for day in range(1, 257):
        counter_copy = Counter()
        for j in range(0, 8):
            counter_copy[j] = counter[j+1]
        counter_copy[6] += counter[0]
        counter_copy[8] = counter[0]
        counter = counter_copy
        if day == 80 or day == 256:
            f = 0
            for j in range(0, 9):
                f += counter[j]
            print(f)

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
