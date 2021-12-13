FILE_NAME = 'day11.dat'
ITERATIONS = 100

grid = []


def flash(x, y):
    update_neighbor(x - 1, y - 1) # Top left
    update_neighbor(x,     y - 1) # Top middle
    update_neighbor(x + 1, y - 1) # Top right

    update_neighbor(x - 1, y)     # Left
    update_neighbor(x + 1, y)     # Right

    update_neighbor(x - 1, y + 1) # Bottom left
    update_neighbor(x,     y + 1) # Bottom middle
    update_neighbor(x + 1, y + 1) # Bottom right


def load_data():
    global grid

    grid.clear()

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    for line in lines:
        row = [int(c) for c in line.strip()]
        grid.append(row)

    pretty_print_grid('Starting Values')


def part1():
    global grid

    load_data()

    flashes = 0

    for i in range(ITERATIONS):
        # Step 1: Update the energy levels
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                grid[y][x] = grid[y][x] + 1
                if grid[y][x] == 10:
                    flash(x, y)

        # Step 2: Count (and reset) the flashes
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    grid[y][x] = 0
                    flashes = flashes + 1

        # pretty_print_grid('After Step ' + str(i + 1))
        # print('Flashes: ' + str(flashes))

    pretty_print_grid('Final Values')

    print('Part 1: ' + str(flashes))


def part2():
    global grid

    load_data()

    iteration = 0
    flashes = 0

    while flashes != 100:
        # Step 1: Update the energy levels
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                grid[y][x] = grid[y][x] + 1
                if grid[y][x] == 10:
                    flash(x, y)

        # Step 2: Count (and reset) the flashes
        flashes = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    grid[y][x] = 0
                    flashes = flashes + 1

        iteration = iteration + 1

    pretty_print_grid('Final Values')

    print('Part 2: ' + str(iteration))


def pretty_print_grid(header):
    print('\n' + header + '\n')
    for row in grid:
        print(row)


def update_neighbor(x, y):
    global grid

    if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        # print('neighbor (' + str(x) + ', ' + str(y) + '): ' + str(grid[y][x]) + '...')
        if grid[y][x] < 10:
            grid[y][x] = grid[y][x] + 1
            if grid[y][x] == 10:
                # print('...flashing! (' + str(x) + ', ' + str(y) + ')')
                flash(x, y)


part1()
part2()