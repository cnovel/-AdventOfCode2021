import time
from collections import Counter


def grow_smart(count_pairs, count_letters, dict_insert):
    new_d = Counter()
    for key, val in count_pairs.items():
        new_letter = dict_insert[key]
        p1 = key[0] + dict_insert[key]
        p2 = dict_insert[key] + key[1]
        for p in [p1, p2]:
            new_d[p] += val
        count_letters[new_letter] += val
    return new_d, count_letters


def get_score(letters):
    minimum = -1
    maximum = -1
    for letter, count in letters.items():
        if maximum == -1:
            maximum = count
        else:
            maximum = maximum if maximum > count else count
        if minimum == -1:
            minimum = count
        else:
            minimum = minimum if minimum < count else count
    return maximum - minimum


def main():
    with open("input_14.txt", 'r') as in14:
        lines = [line.strip() for line in in14.readlines()]
    s = time.time()

    rules = {}
    for line in lines:
        if '>' in line:
            val = line.split(" -> ")
            rules[val[0]] = val[1]

    polymer = lines[0]
    count_pairs = Counter()
    letters = Counter({polymer[0]: 1})
    for i in range(1, len(polymer)):
        k = polymer[i-1] + polymer[i]
        count_pairs[k] += 1
        letters[polymer[i]] += 1
    for i in range(0, 40):
        count_pairs, letters = grow_smart(count_pairs, letters, rules)
        if i == 9 or i == 39:
            print(f"Step {i+1}: {get_score(letters)}")

    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
