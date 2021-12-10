import time


def get_closing(c):
    if c == "(":
        return ")"
    if c == "[":
        return "]"
    if c == "{":
        return "}"
    if c == "<":
        return ">"


def get_points(c):
    if c == ")":
        return 3
    if c == "]":
        return 57
    if c == "}":
        return 1197
    if c == ">":
        return 25137


def get_close_points(c):
    if c == ")":
        return 1
    if c == "]":
        return 2
    if c == "}":
        return 3
    if c == ">":
        return 4


def main():
    with open("input_10.txt", 'r') as in10:
        lines = [line.strip() for line in in10.readlines()]
    s = time.time()

    bad_points = 0
    good_points = []
    for line in lines:
        stack = []
        bad_line = False
        for c in line:
            if c in '([<{':
                stack.append(get_closing(c))
            elif c != stack.pop():
                bad_points += get_points(c)
                bad_line = True
                break
        if bad_line:
            continue
        points = 0
        while len(stack) > 0:
            points = 5 * points + get_close_points(stack.pop())
        good_points.append(points)

    good_points.sort()
    print("Part 1:", bad_points)
    print("Part 2:", sorted(good_points)[int(len(good_points)/2)])
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
