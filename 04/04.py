import time


class Grid:
    def __init__(self, grid_lines):
        parse_lines = [n for n in [line.split() for line in grid_lines]]
        nums = [int(x) for line in parse_lines for x in line]
        self._grid = [[x, False] for x in nums]

    def mark_n(self, i: int):
        for p in self._grid:
            if p[0] == i:
                p[1] = True

    def is_valid(self) -> bool:
        # Lines
        for i in range(0, len(self._grid), 5):
            line_valid = True
            for j in range(i, i+5):
                if not self._grid[j][1]:
                    line_valid = False
                    break
            if line_valid:
                return True

        # Columns
        for i in range(0, 5):
            c_valid = True
            for j in range(0, 21, 5):
                if not self._grid[i+j][1]:
                    c_valid = False
                    break
            if c_valid:
                return True

        return False

    def sum_unmarked(self):
        return sum([x[0] for x in self._grid if not x[1]])


def main():
    with open("input_04.txt", 'r') as in03:
        lines = [line.strip() for line in in03.readlines()]
    s = time.time()

    bingo_nums = [int(x) for x in lines[0].split(',')]
    grids = []
    for i in range(2, len(lines), 6):
        grids.append(Grid(lines[i:i+5]))
    last_score = -1
    for n in bingo_nums:
        for grid in grids:
            grid.mark_n(n)
        for grid in grids:
            if grid.is_valid():
                score = n * grid.sum_unmarked()
                if last_score < 0:
                    print("First grid score", score)
                last_score = score
        grids = [g for g in grids if not g.is_valid()]
    print("Last grid score", last_score)

    print(f"Took {time.time() -s:.3f}s")


if __name__ == '__main__':
    main()
