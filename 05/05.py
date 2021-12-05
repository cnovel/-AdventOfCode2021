import time


def get_lines(lines):
    tmp = [",".join(line.split(" -> ")).split(",") for line in lines]
    res = []
    for t in tmp:
        res.append([int(x) for x in t])
    return res


def get_straight_lines(lines):
    return [seg for seg in lines if seg[0] == seg[2] or seg[1] == seg[3]]


def get_obliques(lines):
    return [seg for seg in lines if seg[0] != seg[2] and seg[1] != seg[3]]


def get_lines_as_point_list(lines):
    pts = []
    for line in lines:
        pt = []
        min_x = min(line[0], line[2])
        max_x = max(line[0], line[2])
        min_y = min(line[1], line[3])
        max_y = max(line[1], line[3])
        if min_x == max_x or min_y == max_y:
            for x in range(min_x, max_x+1):
                for y in range(min_y, max_y+1):
                    pt.append((x, y))
        else:
            step_x = 1 if line[0] < line[2] else -1
            step_y = 1 if line[1] < line[3] else -1
            p = (line[0], line[1])
            while p[0] != line[2] + step_x:
                pt.append(p)
                p = (p[0] + step_x, p[1] + step_y)
        pts.append(pt)

    return pts


def main():
    with open("input_05.txt", 'r') as in05:
        lines = [line.strip() for line in in05.readlines()]
    s = time.time()

    list_lines = get_lines(lines)
    max_x = 0
    max_y = 0
    for line in list_lines:
        max_x = max(max_x, max(line[0], line[2]))
        max_y = max(max_y, max(line[1], line[3]))

    score = [0 for i in range(0, (max_x + 1) * (max_y + 1))]

    straight_lines = get_straight_lines(list_lines)
    for line in get_lines_as_point_list(straight_lines):
        for p in line:
            i = p[0] + (max_x + 1) * p[1]
            score[i] += 1
    print("Part 1:", sum([1 for s in score if s > 1]))

    obliques = get_obliques(list_lines)
    for line in get_lines_as_point_list(obliques):
        for p in line:
            i = p[0] + (max_x + 1) * p[1]
            score[i] += 1
    print("Part 2:", sum([1 for s in score if s > 1]))

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
