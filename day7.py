FILE_NAME = 'day7.dat'

max_value = 0
positions = []

def load_data():
    global max_value, positions

    positions.clear()

    file = open(FILE_NAME, 'r')
    positions = [int(num) for num in file.readlines()[0].strip().split(',')]

    for position in positions:
        if position > max_value:
            max_value = position

    # print(positions)
    # print('Max: ' + str(max_value))


def part1():
    load_data()

    min_cost = max_value * len(positions) # This is bigger than any possible cost

    for i in range(max_value + 1):
        cost = 0
        for position in positions:
            cost = cost + abs(position - i)

        # print('Cost for position ' + str(i) + ': ' + str(cost))

        if cost < min_cost:
            min_cost = cost

    print('Part 1: ' + str(min_cost))


def part2():
    load_data()

    min_cost = max_value * len(positions) * len(positions) # This is bigger than any possible cost

    # print(max_value)
    for i in range(max_value + 1):
        # if i % 100 == 0:
        #     print(i)

        cost = 0
        for position in positions:
            for j in range(1, abs(position - i) + 1):
                cost = cost + j

        # print('Cost for position ' + str(i) + ': ' + str(cost))

        if cost < min_cost:
            min_cost = cost

    print('Part 2: ' + str(min_cost))


part1()
part2()