with open("input_02.txt", 'r') as in01:
    # Part 1
    print("Part 1")
    lines = [line.strip() for line in in01.readlines()]
    x = 0
    y = 0
    for line in lines:
        cmd = line.split(' ')[0]
        value = int(line.split(' ')[1])
        if cmd == "forward":
            x += value
        elif cmd == "down":
            y += value
        else:
            y -= value

    print("X:", x)
    print("Y:", y)
    print("Product:", x*y)

    x = 0
    y = 0
    aim = 0

    print("\nPart 2")
    for line in lines:
        cmd = line.split(' ')[0]
        value = int(line.split(' ')[1])
        if cmd == "forward":
            x += value
            y += aim*value
        elif cmd == "down":
            aim += value
        else:
            aim -= value

    print("X:", x)
    print("Y:", y)
    print("Product:", x*y)