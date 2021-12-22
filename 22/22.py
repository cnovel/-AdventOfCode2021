import time


def part_1(lines):
    count = set()
    for line in lines:
        min_x = max(-50, line[1][0])
        min_y = max(-50, line[1][2])
        min_z = max(-50, line[1][4])
        max_x = min(50, line[1][1])
        max_y = min(50, line[1][3])
        max_z = min(50, line[1][5])
        if min_x > max_x or min_y > max_y or min_z > max_z:
            continue  # Invalid interval

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    if line[0] == 'on':
                        count.add((x, y, z))
                    elif (x, y, z) in count:
                        count.remove((x, y, z))

    print("Part 1:", len(count))


class Cube:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max

    def engulf(self, cube):
        return self.x_min <= cube.x_min and self.y_min <= cube.y_min and self.z_min <= cube.z_min and \
               self.x_max >= cube.x_max and self.y_max >= cube.y_max and self.z_max >= cube.z_max

    def intersects(self, cube):
        min_x = max(self.x_min, cube.x_min)
        min_y = max(self.y_min, cube.y_min)
        min_z = max(self.z_min, cube.z_min)
        max_x = min(self.x_max, cube.x_max)
        max_y = min(self.y_max, cube.y_max)
        max_z = min(self.z_max, cube.z_max)
        return min_x <= max_x and min_y <= max_y and min_z <= max_z

    def size(self):
        return (self.x_max + 1 - self.x_min) * (self.y_max + 1 - self.y_min) * (self.z_max + 1 - self.z_min)

    def add(self, cube) -> list:  # Returns a list of new lit cubes
        if not self.intersects(cube):
            return [cube]

        cubes = []
        xs = sorted([self.x_min, self.x_max, cube.x_min, cube.x_max])
        ys = sorted([self.y_min, self.y_max, cube.y_min, cube.y_max])
        zs = sorted([self.z_min, self.z_max, cube.z_min, cube.z_max])
        for i in range(0, len(xs) - 1):
            min_x = xs[i]
            max_x = xs[i+1] - 1 if i != len(xs) - 2 else xs[i+1]  # We want to create disjoint cubes
            if min_x > max_x:
                continue
            for j in range(0, len(ys) - 1):
                min_y = ys[j]
                max_y = ys[j+1] - 1 if j != len(ys) - 2 else ys[j+1]  # We want to create disjoint cubes
                if min_y > max_y:
                    continue
                for k in range(0, len(zs) - 1):
                    min_z = zs[k]
                    max_z = zs[k+1] - 1 if k != len(zs) - 2 else zs[k+1]  # We want to create disjoint cubes
                    if min_z > max_z:
                        continue
                    c = Cube(min_x, max_x, min_y, max_y, min_z, max_z)
                    if not self.engulf(c) and cube.engulf(c):
                        cubes.append(c)
        return cubes

    def delete(self, cube) -> list:
        if cube.engulf(self):
            return []
        if not self.intersects(cube):
            return [cube]

        cubes = []
        xs = sorted([self.x_min, self.x_max, cube.x_min, cube.x_max])
        ys = sorted([self.y_min, self.y_max, cube.y_min, cube.y_max])
        zs = sorted([self.z_min, self.z_max, cube.z_min, cube.z_max])
        for i in range(0, len(xs) - 1):
            min_x = xs[i]
            max_x = xs[i+1] - 1 if i != len(xs) - 2 else xs[i+1]
            if min_x > max_x:
                continue
            for j in range(0, len(ys) - 1):
                min_y = ys[j]
                max_y = ys[j+1] - 1 if j != len(ys) - 2 else ys[j+1]
                if min_y > max_y:
                    continue
                for k in range(0, len(zs) - 1):
                    min_z = zs[k]
                    max_z = zs[k+1] - 1 if k != len(zs) - 2 else zs[k+1]
                    if min_z > max_z:
                        continue
                    c = Cube(min_x, max_x, min_y, max_y, min_z, max_z)
                    if self.engulf(c) and not cube.engulf(c):
                        cubes.append(c)
        return cubes


def part_2(lines):
    cubes = [Cube(lines[0][1][0], lines[0][1][1], lines[0][1][2], lines[0][1][3], lines[0][1][4], lines[0][1][5])]
    for i in range(1, len(lines)):
        print(f"Line {i+1}/{len(lines)}, {len(cubes)} cubes")
        line = lines[i]
        newly_lit_cubes = [Cube(line[1][0], line[1][1], line[1][2], line[1][3], line[1][4], line[1][5])]
        new_cubes = []

        if line[0] == 'on':
            for cube in cubes:
                newly_lit_cubes_bis = []
                for newly_lit_cube in newly_lit_cubes:
                    newly_lit_cubes_bis += cube.add(newly_lit_cube)
                newly_lit_cubes = newly_lit_cubes_bis
            new_cubes = cubes + newly_lit_cubes
        else:
            for cube in cubes:
                new_cubes += cube.delete(newly_lit_cubes[0])
        cubes = new_cubes
    score = sum([c.size() for c in cubes])
    print("Part 2:", score)


def main():
    with open("input_22test.txt", 'r') as in22:
        lines = [line.strip() for line in in22.readlines()]
    s = time.time()

    lines = [line.split(" ") for line in lines]
    lines = [(line[0], line[1].split(",")) for line in lines]
    new_lines = []
    for line in lines:
        coords = line[1]
        new_coords = []
        for coord in coords:
            c = coord[2:].split("..")
            for m in c:
                new_coords.append(int(m))
        new_lines.append((line[0], new_coords))
    lines = new_lines

    part_1(lines)
    part_2(lines)

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
