FILE_NAME = 'day12-small.dat'

graph = {}


def load_data():
    global graph

    graph.clear()

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    for line in lines:
        endpoints = line.strip().split('-')

        # Add the link from point A to B
        if endpoints[0] in graph:
            connections = graph.get(endpoints[0])
            connections.append(endpoints[1])
        else:
            connections = [ endpoints[1] ]
            graph[endpoints[0]] = connections

        # Add the reverse link from point B to A
        if endpoints[1] in graph:
            connections = graph.get(endpoints[1])
            connections.append(endpoints[0])
        else:
            connections = [ endpoints[0] ]
            graph[endpoints[1]] = connections

    print(graph)


def part1():
    global graph

    load_data()

    paths = 0

    print('Part 1: ' + str(paths))


def part2():
    print('Part 2: ' + str(0))


part1()
part2()