FILE_NAME = 'day12.dat'

graph = {}


def count_paths(start, visited, this_path):
    connections = graph.get(start)

    paths = 0

    for node in connections:
        if node == 'end':
            this_path.append(node)
            # print(this_path)
            paths = paths + 1
        elif node != node.lower() or node not in visited:
            this_path_copy = this_path.copy()
            this_path_copy.append(node)
            visited_copy = visited.copy()
            visited_copy.add(node)
            paths = paths + count_paths(node, visited_copy, this_path_copy)

    return paths


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

    # print(graph)


def part1():
    global graph

    load_data()

    visited = set()
    visited.add('start')
    paths = count_paths('start', visited, ['start'])

    print('Part 1: ' + str(paths))


def part2():
    print('Part 2: ' + str(0))


part1()
part2()
