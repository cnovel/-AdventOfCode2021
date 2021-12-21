import time
from collections import Counter


def update_pos(pos, move):
    new_pos = pos + move
    new_pos = new_pos % 10
    if new_pos == 0:
        new_pos = 10
    return new_pos


def get_wins_count(positions_init, possible_moves):
    wins = [0, 0]
    scores = Counter()
    scores[((positions_init[0], 0), (positions_init[1], 0))] = 1
    while len(scores.keys()) > 0:
        new_scores = Counter()
        # Update J1
        for move, nb in possible_moves.items():
            for key in scores.keys():
                new_pos = update_pos(key[0][0], move)
                new_score = key[0][1] + new_pos
                new_key = ((new_pos, new_score), key[1])
                if new_score >= 21:
                    wins[0] += scores[key] * nb
                else:
                    new_scores[new_key] += scores[key] * nb
        scores = new_scores

        new_scores = Counter()
        # Update J2
        for move, nb in possible_moves.items():
            for key in scores.keys():
                new_pos = update_pos(key[1][0], move)
                new_score = key[1][1] + new_pos
                new_key = (key[0], (new_pos, new_score))
                if new_score >= 21:
                    wins[1] += scores[key] * nb
                else:
                    new_scores[new_key] += scores[key] * nb
        scores = new_scores

    return wins


def update_dice(dice):
    dice = [d + 3 for d in dice]
    return [d if d <= 100 else d - 100 for d in dice]


def main():
    with open("input_21.txt", 'r') as in21:
        lines = [line.strip() for line in in21.readlines()]
    s = time.time()

    positions = [int(lines[0].split(" ")[-1]), int(lines[1].split(" ")[-1])]
    scores = [0, 0]

    dice = [1, 2, 3]
    roll = 3
    while True:
        # Move first player
        positions[0] = update_pos(positions[0], sum(dice))
        scores[0] += positions[0]
        if scores[0] >= 1000:
            break

        dice = update_dice(dice)
        roll += 3

        positions[1] = update_pos(positions[1], sum(dice))
        scores[1] += positions[1]
        if scores[1] >= 1000:
            break

        dice = update_dice(dice)
        roll += 3

    if scores[0] >= 1000:
        print(f"Part 1: {roll * scores[1]}")
    else:
        print(f"Part 1: {roll * scores[0]}")

    positions = [int(lines[0].split(" ")[-1]), int(lines[1].split(" ")[-1])]
    possible_moves = []
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                possible_moves.append([i, j, k])
    possible_moves = [sum(dices) for dices in possible_moves]
    possible_moves = Counter(possible_moves)

    print("Part 2:", max(get_wins_count(positions, possible_moves)))
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
