def part1():
    x = 0
    y = 0

    file = open('day2.dat', 'r')
    lines = file.readlines()

    for line in lines:
        parts = line.strip().split(' ')
        command = parts[0]
        value = int(parts[1])

        if command == 'forward':
            x = x + value
        elif command == 'down':
            y = y + value
        else:
            y = y - value

    product = x * y

    print("Part 1: " + str(product))


def part2():
    aim = 0
    x = 0
    y = 0

    file = open('day2.dat', 'r')
    lines = file.readlines()

    for line in lines:
        parts = line.strip().split(' ')
        command = parts[0]
        value = int(parts[1])

        if command == 'forward':
            x = x + value
            y = y + (value * aim)
        elif command == 'down':
            aim = aim + value
        else:
            aim = aim - value

    product = x * y

    print("Part 2: " + str(product))


part1()
part2()