def part1():
    file = open('day1.dat', 'r')
    lines = file.readlines()

    lastNumber = 100000

    count = 0

    for line in lines:
        number = int(line.strip())

        if number > lastNumber:
            count = count + 1

        lastNumber = number

    print("Part 1: " + str(count))


def part2():
    # Step 1: Create a new array of "triplets"
    sums = []

    file = open('day1.dat', 'r')
    lines = file.readlines()

    for i in range(2, len(lines), 1):
        total = int(lines[i]) + int(lines[i - 1]) + int(lines[i - 2])
        sums.append(total)

    # Step 2: Now analyze those triplets
    lastSum = 100000

    count = 0

    for sum in sums:
        if sum > lastSum:
            count = count + 1

        lastSum = sum

    print("Part 2: " + str(count))


part1()
part2()