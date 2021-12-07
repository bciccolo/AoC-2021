FILE_NAME = 'day5.dat'
GRAPH_SIZE = 1000

coordinate_plane = []
coordinates_list = []


def count_intersections():
    count = 0

    for row in coordinate_plane:
        for col in row:
            if col > 1:
                count = count + 1

    return count


def horizontal_vertical(coordinates):
    return coordinates[0][0] == coordinates[1][0] or coordinates[0][1] == coordinates[1][1]


def load_data():
    global coordinate_plane, coordinates_list

    # Step 1: Initialize the coordinate plane
    coordinate_plane.clear()

    for y in range(GRAPH_SIZE):
        row = []
        for x in range(GRAPH_SIZE):
            row.append(0)
        coordinate_plane.append(row)

    # Step 2: Initialize the list of coordinates from the data file
    coordinates_list.clear()

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    for line in lines:
        points = line.strip().split('->')
        p1 = points[0].split(',')
        p2 = points[1].split(',')

        start = [int(p1[0]), int(p1[1])];
        end =   [int(p2[0]), int(p2[1])];

        coordinates = [start, end]
        coordinates_list.append(coordinates)

    # Test results
    # print_plane()
    # print(coordinates_list)


def part1():
    global coordinate_plane, coordinates_list

    load_data()

    # Only plot the horizontal and vertical lines for part 1
    coordinates_list = [coordinates for coordinates in coordinates_list if horizontal_vertical(coordinates)]
    plot_coordinates()

    # print_plane()
    # print(coordinates_list)

    # Count the spaces greater than 1
    print('Part 1: ' + str(count_intersections()))


def part2():
    global coordinate_plane, coordinates_list

    load_data()

    plot_coordinates()

    # print_plane()
    # print(coordinates_list)

    # Count the spaces greater than 1
    print('Part 2: ' + str(count_intersections()))


def plot_coordinates():
    global coordinate_plane, coordinates_list

    for coordinates in coordinates_list:
        start = coordinates[0]
        end = coordinates[1]

        # If x values match we have a vertical line
        if start[0] == end[0]:
            x = start[0]
            minY = start[1] if start[1] < end[1] else end[1]
            maxY = start[1] if start[1] > end[1] else end[1]
            for y in range(minY, maxY + 1):
                coordinate_plane[y][x] = coordinate_plane[y][x] + 1

        # If y values match we have a horizontal line
        elif start[1] == end[1]:
            y = start[1]
            minX = start[0] if start[0] < end[0] else end[0]
            maxX = start[0] if start[0] > end[0] else end[0]
            for x in range(minX, maxX + 1):
                coordinate_plane[y][x] = coordinate_plane[y][x] + 1

        # If neither match then we have a (perfectly 45 degree) diagonal line
        else:
            distance = abs(start[0] - end[0]) + 1
            dx = -1 if start[0] > end[0] else 1
            dy = -1 if start[1] > end[1] else 1

            # print(start)
            # print(end)
            # print('dx: ' + str(dx) + ', dy: ' + str(dy))

            for i in range(distance):
                x = start[0] + dx * i
                y = start[1] + dy * i
                coordinate_plane[y][x] = coordinate_plane[y][x] + 1


def print_plane():
    global coordinate_plane

    print('+---------------------+')
    for row in coordinate_plane:
        display = '| '
        for col in row:
            if col > 0:
                display = display + str(col) + ' '
            else:
                display = display + '. '
        display = display + '|'
        print(display)
    print('+---------------------+')


part1()
part2()