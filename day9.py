FILE_NAME = 'day9.dat'

BORDER = 9
CHECKED = -1

height_map = []


def load_data():
    global height_map

    height_map.clear()

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    for line in lines:
        row = [int(c) for c in line.strip()]
        height_map.append(row)

    # print(height_map)


def find_low_points():
    low_points = []

    max_y = len(height_map) - 1
    max_x = len(height_map[0]) - 1

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            height = height_map[y][x]

            if x == 0 and y == 0:
                # top-left corner
                if (height < height_map[y][x + 1] and
                    height < height_map[y + 1][x]):
                    # print('found top-left corner: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)
            elif x == 0 and y == max_y:
                # bottom-left corner
                if (height < height_map[y][x + 1] and
                    height < height_map[y - 1][x]):
                    # print('found bottom-left corner: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)
            elif x == max_x and y == 0:
                # top-right corner
                if (height < height_map[y][x - 1] and
                    height < height_map[y + 1][x]):
                    # print('found top-right corner: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)
            elif x == max_x and y == max_y:
                # bottom-right corner
                if (height < height_map[y][x - 1] and
                    height < height_map[y - 1][x]):
                    # print('found bottom-right corner: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)
            elif x == 0:
                # left edge
                if (height < height_map[y - 1][x] and
                    height < height_map[y + 1][x] and
                    height < height_map[y][x + 1]):
                    # print('found left edge: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)
            elif x == max_x:
                # right edge
                if (height < height_map[y - 1][x] and
                    height < height_map[y + 1][x] and
                    height < height_map[y][x - 1]):
                    # print('found right edge: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)
            elif y == 0:
                # top edge
                if (height < height_map[y][x - 1] and
                    height < height_map[y][x + 1] and
                    height < height_map[y + 1][x]):
                    # print('found top edge: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)
            elif y == max_y:
                # bottom edge
                if (height < height_map[y][x - 1] and
                    height < height_map[y][x + 1] and
                    height < height_map[y - 1][x]):
                    # print('found bottom edge: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)
            else:
                # interior
                if (height < height_map[y][x - 1] and
                    height < height_map[y][x + 1] and
                    height < height_map[y - 1][x] and
                    height < height_map[y + 1][x]):
                    # print('found interior: ' + str(height) + ' at ' + str(x) + ', ' + str(y))
                    low_points.append(height)

    return low_points


def part1():
    load_data()

    low_points = find_low_points()

    risk_total = 0
    for low_point in low_points:
        risk_total = risk_total + low_point + 1

    print('Part 1: ' + str(risk_total))


def part2():
    load_data()

    # basin_sizes = find_basin_sizes()

    print('Part 2: ' + str(0))


part1()
part2()