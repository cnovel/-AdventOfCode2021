import time


class Scanner:
    def __init__(self, i):
        self.id = i
        self.transfo = [1, 1, 1]
        self.position = [0, 0, 0]
        self.beacons = []
        self.matched = False

    def add_beacon(self, beacon):
        self.beacons.append(beacon)

    def get_beacons_real_coords(self):
        b = []
        for beacon in self.beacons:
            new_pos = [beacon[0] * self.transfo[0], beacon[1] * self.transfo[1], beacon[2] * self.transfo[2]]
            new_pos = [new_pos[0] + self.position[0], new_pos[1] + self.position[1], new_pos[2] + self.position[2]]
            b.append(new_pos)
        return b

    def get_beacon_coord(self, beacon):
        new_pos = [beacon[0] * self.transfo[0], beacon[1] * self.transfo[1], beacon[2] * self.transfo[2]]
        new_pos = [new_pos[0] + self.position[0], new_pos[1] + self.position[1], new_pos[2] + self.position[2]]
        return new_pos

    def set_origin_by_matching(self, real_beacon_pos, beacon_relative):
        # real - rel * transfo
        origin = [beacon_relative[0] * self.transfo[0], beacon_relative[1] * self.transfo[1],
                  beacon_relative[2] * self.transfo[2]]
        origin = [real_beacon_pos[0] - origin[0], real_beacon_pos[1] - origin[1], real_beacon_pos[2] - origin[2]]
        self.position = origin


def try_match(scan_a, scan_b):
    transfos = []
    for i in [-1, 1]:
        for j in [-1, 1]:
            for k in [-1, 1]:
                transfos.append([i, j, k])
    set_a = set(tuple(i) for i in scan_a.get_beacons_real_coords())
    for transfo in transfos:
        scan_b.transfo = transfo
        for real_beacon_a in set_a:
            for beacon_b in scan_b.beacons:
                # We want to put beacon_b on beacon_a
                scan_b.set_origin_by_matching(real_beacon_a, beacon_b)
                set_b = set(tuple(i) for i in scan_b.get_beacons_real_coords())
                print("Overlapping =", len(set_a.intersection(set_b)))
                if len(set_a.intersection(set_b)) >= 12:
                    scan_b.matched = True
                    return


def main():
    with open("input_19test.txt", 'r') as in19:
        lines = [line.strip() for line in in19.readlines()]
    s = time.time()

    scans = []
    for line in lines:
        if 'scanner' in line:
            s = Scanner(int(line.split(' ')[2]))
            scans.append(s)
            continue

        if ',' in line:
            beacon = [int(x) for x in line.split(",")]
            scans[-1].add_beacon(beacon)

    scans[0].matched = True
    while sum([0 if scan.matched else 1 for scan in scans]) > 0:
        for i in range(0, len(scans)):
            for j in range(i+1, len(scans)):
                if scans[i].matched and (not scans[j].matched):
                    try_match(scans[i], scans[j])
                if scans[j].matched and (not scans[i].matched):
                    try_match(scans[j], scans[i])

    beacons = set()
    for scan in scans:
        b = scan.get_beacons_real_coords()
        beacons.update(set(tuple(i) for i in b))
    print(len(beacons))
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
