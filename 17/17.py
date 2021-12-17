import time
import re


def find_possible_vx(x_min, x_max):
    min_vx = [x for x in range(0, x_max+1) if x_min <= x * (x + 1) / 2 <= x_max][0]
    valid_window_vx = {}
    for vx in range(min_vx, x_max+1):
        x = 0
        v = vx
        step = 0
        valid_steps = []
        while x < x_max and v > 0:
            x += v
            v -= 1
            step += 1
            if x_min <= x <= x_max:
                valid_steps.append(step)
        if len(valid_steps) == 0:
            continue

        if v == 0:
            valid_steps = (valid_steps[0], 10000000000000000000000000)  # Absurdly big int for infinity
        else:
            valid_steps = (valid_steps[0], valid_steps[-1])
        valid_window_vx[vx] = valid_steps
    return valid_window_vx


def find_possible_vy(y_min, y_max, v_max):
    valid_window_vy = {}
    for vy in range(y_min, v_max+1):
        y = 0
        v = vy
        step = 0
        valid_steps = []
        while y > y_min:
            y += v
            v -= 1
            step += 1
            if y_min <= y <= y_max:
                valid_steps.append(step)
        if len(valid_steps) == 0:
            continue
        valid_steps = (valid_steps[0], valid_steps[-1])
        valid_window_vy[vy] = valid_steps
    return valid_window_vy


def nb_possible_velocities(valid_window_vx, valid_window_vy):
    velocities = []
    for vx, wx in valid_window_vx.items():
        for vy, wy in valid_window_vy.items():
            min_step = max(wx[0], wy[0])
            max_step = min(wx[1], wy[1])
            if min_step <= max_step:
                velocities.append((vx, vy))
    return len(velocities)


def main():
    with open("input_17.txt", 'r') as in17:
        lines = [line.strip() for line in in17.readlines()]
    s = time.time()

    box = [int(x) for x in re.findall(r'\d+', lines[0])]
    box[2] = -box[2]
    box[3] = -box[3]

    max_vy = -box[2] - 1
    max_height = int(max_vy * (max_vy + 1) / 2)
    print(f"Part 1: {max_height}m with max_vy = {max_vy}")

    # Find all possible velocities
    possible_vx = find_possible_vx(box[0], box[1])
    possible_vy = find_possible_vy(box[2], box[3], max_vy)
    nb = nb_possible_velocities(possible_vx, possible_vy)
    print(f"Part 2: {nb} possible velocities")
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
