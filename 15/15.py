import time


def increment_line(line, n=1):
    new_line = []
    for x in line:
        y = x + n
        if y > 9:
            y = y - 9
        new_line.append(y)
    return new_line


def main():
    with open("input_15.txt", 'r') as in15:
        lines = [line.strip() for line in in15.readlines()]
    s = time.time()

    lines = [[int(x) for x in line] for line in lines]

    """
    height = len(lines)
    for n in range(1, 5):
        for line in lines[0:height]:
            lines.append(increment_line(line, n))

    new_lines = []
    for line in lines:
        line = line + increment_line(line, 1) + increment_line(line, 2) \
               + increment_line(line, 3) + increment_line(line, 4)
        new_lines.append(line)

    lines = new_lines
    """

    dist = {}
    q = []
    width = len(lines[0])
    height = len(lines)
    for i in range(0, width):
        for j in range(0, height):
            dist[(i, j)] = -1
            q.append((i, j))
    dist[(0, 0)] = 0

    find_total = 0
    pop_time = 0
    neigh_time = 0
    while len(q) > 0:
        pt = (-1, -1)
        best_dist = -1
        start = time.time()
        for p in q:
            if dist[p] != -1:
                if best_dist == -1 or dist[p] < best_dist:
                    best_dist = dist[p]
                    pt = p
        find_total += time.time() - start
        start = time.time()
        q.remove(pt)
        pop_time += time.time() - start
        if pt == (width-1, height-1):
            print(f"Dist part 1 = {dist[(width-1, height-1)]}")
        start = time.time()
        neighs = [(pt[0] - 1, pt[1]), (pt[0] + 1, pt[1]), (pt[0], pt[1] - 1), (pt[0], pt[1] + 1)]
        neighs = [n for n in neighs if n in q]
        neigh_time += time.time() - start
        for n in neighs:
            d = dist[pt] + lines[n[1]][n[0]]
            if d < dist[n] or dist[n] == -1:
                dist[n] = d
    print(dist[(width-1, height-1)])
    print("Find total:", find_total)
    print("Pop:", pop_time)
    print("Neigh:", neigh_time)
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
