FILE_NAME = 'day13.dat'

coordinates = []
folds = []
display_x = 0
display_y = 0
max_x = 0
max_y = 0


def fold(grid, count):
    global display_x, display_y

    for i in range(count):
        fold = folds[i]

        if fold[0] == 'y':
            display_y = fold[1]

            for y in range(fold[1] + 1, max_y + 1):
                for x in range(max_x + 1):
                    if grid[y][x] == '#':
                        new_y = fold[1] - (y - fold[1])
                        if new_y >= 0:
                            grid[new_y][x] = '#'

                            # Clear the # to facilitate easier counting later
                            grid[y][x] = '.'
        else: # fold[0] == 'x'
            display_x = fold[1]

            for y in range(max_y + 1):
                for x in range(fold[1] + 1, max_x + 1):
                    if grid[y][x] == '#':
                        new_x = fold[1] - (x - fold[1])
                        if new_x >= 0:
                            grid[y][new_x] = '#'

                            # Clear the # to facilitate easier counting later
                            grid[y][x] = '.'


def load_data():
    global coordinates, max_x, max_y, folds, display_x, display_y

    # Parse the file into two structures: coordinates and fold instructions
    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    found_blank = False

    for line in lines:
        line = line.strip()

        if line == '':
            found_blank = True
        else:
            if found_blank:
                instructions = line[11:].split('=')
                folds.append([instructions[0], int(instructions[1])])
            else:
                coordinate = [int(x) for x in line.split(',')]

                if coordinate[0] > max_x:
                    max_x = coordinate[0]

                if coordinate[1] > max_y:
                    max_y = coordinate[1]

                coordinates.append(coordinate)

    display_x = max_x + 1
    display_y = max_y + 1

    # print(coordinates)
    # print(folds)
    # print('Max X: ' + str(max_x))
    # print('Max Y: ' + str(max_y))


def part1():
    grid = plot_coordinates()

    # pretty_print(grid, 'Initial')

    fold(grid, 1)

    # pretty_print(grid, 'After 1 Fold')

    count = 0
    for row in grid:
        for col in row:
            if col == '#':
                count = count + 1

    print('Part 1: ' + str(count))


def part2():
    grid = plot_coordinates()

    fold(grid, len(folds))

    print('Part 2: ')
    pretty_print(grid, 'Final Code')


def plot_coordinates():
    grid = [['.' for col in range(max_x + 1)] for row in range(max_y + 1)]

    for coordinate in coordinates:
        x = coordinate[0]
        y = coordinate[1]
        grid[y][x] = '#'

    return grid


def pretty_print(grid, header):
    print('\n' + header + '\n')
    for y in range(display_y):
        row = "".join(grid[y])
        print(row[:display_x])


load_data()
part1()
part2()