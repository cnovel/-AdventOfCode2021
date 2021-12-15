import time


def increment_line(line, n=1):
    new_line = []
    for x in line:
        y = x + n
        if y > 9:
            y = y - 9
        new_line.append(y)
    return new_line


def neighbors(i, width, height):
    y = int(i / width)
    x = i - width*y
    n = []
    if x-1 >= 0:
        n.append(x-1 + y * width)
    if x+1 < width:
        n.append(x+1 + y * width)
    if y-1 >= 0:
        n.append(x + (y-1) * width)
    if y+1 < height:
        n.append(x + (y+1) * width)
    return n


def dijkstra(lines):
    cost = [x for line in lines for x in line]
    width = len(lines[0])
    height = len(lines)

    dist = [-1] * (width * height)
    visited = [False] * (width * height)
    dist[0] = 0

    to_visit = width * height
    modified_pt = {0}
    while to_visit > 0:
        pt = (-1, -1)
        best_dist = -1
        # Find next point to consider
        for p in modified_pt:
            if best_dist == -1 or dist[p] < best_dist:
                best_dist = dist[p]
                pt = p

        # Mark it as visited
        visited[pt] = True
        modified_pt.remove(pt)
        to_visit -= 1

        # Retrieve unvisited neighbors and update distance
        neighs = set([n for n in neighbors(pt, width, height) if not visited[n]])
        modified_pt = modified_pt.union(neighs)
        for n in neighs:
            d = dist[pt] + cost[n]
            if d < dist[n] or dist[n] == -1:
                dist[n] = d

    return dist[width*height - 1]


def main():
    with open("input_15.txt", 'r') as in15:
        lines = [line.strip() for line in in15.readlines()]
    s = time.time()

    lines = [[int(x) for x in line] for line in lines]
    print("Part 1:", dijkstra(lines))
    print(f"Took {time.time() - s:.3f}s")

    height = len(lines)
    for n in range(1, 5):
        for line in lines[0:height]:
            lines.append(increment_line(line, n))
    new_lines = []
    for line in lines:
        line = line + increment_line(line, 1) + increment_line(line, 2) \
               + increment_line(line, 3) + increment_line(line, 4)
        new_lines.append(line)
    print("Part 2:", dijkstra(new_lines))

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
