import time


def dump(matrix):
    for line in matrix:
        print(''.join(['#' if x else ' ' for x in line]))


def fold_x(matrix, n):
    new_matrix = []
    for line in matrix:
        new_line = line[0:n]
        for i in range(n + 1, len(matrix[0])):
            new_i = 2*n - i
            new_line[new_i] = line[new_i] or line[i]
        new_matrix.append(new_line)
    return new_matrix


def fold_y(matrix, n):
    new_matrix = []
    for j in range(0, n):
        new_matrix.append(matrix[j])
    for j in range(n+1, len(matrix)):
        new_j = 2*n - j
        new_matrix[new_j] = [a or b for a, b in zip(matrix[new_j], matrix[j])]
    return new_matrix


def count(matrix):
    c = 0
    for line in matrix:
        c += line.count(True)
    return c


def main():
    with open("input_13.txt", 'r') as in13:
        lines = [line.strip() for line in in13.readlines()]
    s = time.time()

    dots = []
    folds = []
    for line in lines:
        if ',' in line:
            val = line.split(',')
            dots.append([int(val[0]), int(val[1])])
        if '=' in line:
            val = line.split('=')
            folds.append([val[0][-1], int(val[1])])

    # Create Matrix
    max_x = max([x[0] for x in dots]) + 1
    max_y = max([x[1] for x in dots]) + 1
    matrix = []
    for i in range(0, max_y):
        matrix.append([False] * max_x)
    for dot in dots:
        matrix[dot[1]][dot[0]] = True

    # Fold matrix
    first = True
    for fold in folds:
        if fold[0] == 'x':
            matrix = fold_x(matrix, fold[1])
        else:
            matrix = fold_y(matrix, fold[1])
        if first:
            print("Count", count(matrix))
            first = False

    dump(matrix)
    print(f"Took {time.time() - s:.3f}s")


if __name__ == '__main__':
    main()
