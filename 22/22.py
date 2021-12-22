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

    def _get_cubes(self, cube):
        cubes = []
        x_pairs = ((min(self.x_min, cube.x_min), max(self.x_min, cube.x_min) - 1),
                   (max(self.x_min, cube.x_min), min(self.x_max, cube.x_max)),
                   (min(self.x_max, cube.x_max) + 1, max(self.x_max, cube.x_max)))
        y_pairs = ((min(self.y_min, cube.y_min), max(self.y_min, cube.y_min) - 1),
                   (max(self.y_min, cube.y_min), min(self.y_max, cube.y_max)),
                   (min(self.y_max, cube.y_max) + 1, max(self.y_max, cube.y_max)))
        z_pairs = ((min(self.z_min, cube.z_min), max(self.z_min, cube.z_min) - 1),
                   (max(self.z_min, cube.z_min), min(self.z_max, cube.z_max)),
                   (min(self.z_max, cube.z_max) + 1, max(self.z_max, cube.z_max)))
        
        for x_pair in x_pairs:
            if x_pair[1] < x_pair[0]:
                continue
            for y_pair in y_pairs:
                if y_pair[1] < y_pair[0]:
                    continue
                for z_pair in z_pairs:
                    if z_pair[1] < z_pair[0]:
                        continue
                    cubes.append(Cube(x_pair[0], x_pair[1], y_pair[0], y_pair[1], z_pair[0], z_pair[1]))
        return cubes

    def add(self, cube) -> list:  # Returns a list of newly lit cubes
        if not self.intersects(cube):
            return [cube]

        cubes = []
        for sub_cube in self._get_cubes(cube):
            if cube.engulf(sub_cube) and not self.engulf(sub_cube):
                cubes.append(sub_cube)
        return cubes

    def delete(self, cube) -> list: # Return a list of still lit cubes
        if cube.engulf(self):
            return []
        if not self.intersects(cube):
            return [self]

        cubes = []
        for sub_cube in self._get_cubes(cube):
            if self.engulf(sub_cube) and not cube.engulf(sub_cube):
                cubes.append(sub_cube)
        return cubes


def part_2(lines):
    cubes = [Cube(lines[0][1][0], lines[0][1][1], lines[0][1][2], lines[0][1][3], lines[0][1][4], lines[0][1][5])]
    for i in range(1, len(lines)):
        #print(f"Line {i+1}/{len(lines)}, {len(cubes)} cubes")
        line = lines[i]
        current_cube = Cube(line[1][0], line[1][1], line[1][2], line[1][3], line[1][4], line[1][5])
        new_cubes = []

        if line[0] == 'on':
            newly_lit_cubes = [current_cube]
            for cube in cubes:
                newly_lit_cubes_bis = []
                for newly_lit_cube in newly_lit_cubes:
                    newly_lit_cubes_bis += cube.add(newly_lit_cube)
                newly_lit_cubes = newly_lit_cubes_bis
            new_cubes = cubes + newly_lit_cubes
        else:
            for lit_cube in cubes:
                new_cubes += lit_cube.delete(current_cube)

        cubes = new_cubes

    score = sum([c.size() for c in cubes])
    print("Part 2:", score)


def main():
    with open("input_22.txt", 'r') as in22:
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
