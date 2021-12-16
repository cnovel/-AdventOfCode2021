import time


def bin_to_int(s):
    return int(s, 2)


def get_value_from_bits(bits_by_five):
    return bin_to_int(''.join([b[1:] for b in bits_by_five]))


def product(elements):
    p = 1
    for i in elements:
        p = p * i
    return p


class Packet:
    def __init__(self, line):
        self.ver = bin_to_int(line[0:3])
        self.type = bin_to_int(line[3:6])
        self.total_length = 6  # Version + Type bits
        self.sub_packets = []
        self.bits_by_five = []
        if self.type == 4:
            self.bits_by_five = [line[6:11]]
            i = 11
            while self.bits_by_five[-1][0] == '1':
                self.bits_by_five.append(line[i:i + 5])
                i += 5
            self.total_length += 5*len(self.bits_by_five)
            return

        self.total_length += 1  # I bit
        if line[6] == '0':
            # First case
            len_sub_pack = bin_to_int(line[7:22])
            self.total_length += 15 + len_sub_pack  # Length of L + length of sub packets
            while sum(p.total_length for p in self.sub_packets) < len_sub_pack:
                self.sub_packets.append(Packet(line[22+sum(p.total_length for p in self.sub_packets):]))
        else:
            # Second case
            self.total_length += 11  # Length of L
            nb_sub_packages = bin_to_int(line[7:18])
            while len(self.sub_packets) != nb_sub_packages:
                self.sub_packets.append(Packet(line[18 + sum(p.total_length for p in self.sub_packets):]))
            self.total_length += sum(p.total_length for p in self.sub_packets)

    def summed_version(self):
        return self.ver + sum([x.summed_version() for x in self.sub_packets])

    def get_value(self):
        if self.type == 4:
            return get_value_from_bits(self.bits_by_five)
        if self.type == 0:
            return sum([p.get_value() for p in self.sub_packets])
        if self.type == 1:
            return product([p.get_value() for p in self.sub_packets])
        if self.type == 2:
            return min([p.get_value() for p in self.sub_packets])
        if self.type == 3:
            return max([p.get_value() for p in self.sub_packets])
        values = [self.sub_packets[0].get_value(), self.sub_packets[1].get_value()]
        if self.type == 5:
            return 1 if values[0] > values[1] else 0
        if self.type == 6:
            return 1 if values[0] < values[1] else 0
        if self.type == 7:
            return 1 if values[0] == values[1] else 0


def main():
    with open("input_16.txt", 'r') as in16:
        lines = [line.strip() for line in in16.readlines()]
    s = time.time()

    line = lines[0]
    to_binary = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }
    bin_line = ''.join([to_binary[x] for x in line])

    main_packet = Packet(bin_line)
    print("Part 1:", main_packet.summed_version())
    print("Part 2:", main_packet.get_value())
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
