FILE_NAME = 'day12.dat' # Part 1 results: 10, 19, 226, 3713

graph = {}
small_caves = set()


def find_paths(start, visited, this_path, revisit, all_paths):
    connections = graph.get(start)

    for node in connections:
        if node == 'end':
            this_path.append(node)
            all_paths.add(",".join(this_path))
        elif node == node.upper() or node not in visited or node == revisit:
            this_path_copy = this_path.copy()
            this_path_copy.append(node)
            visited_copy = visited.copy()

            if node == revisit:
                find_paths(node, visited_copy, this_path_copy, None, all_paths)
            else:
                visited_copy.add(node)
                find_paths(node, visited_copy, this_path_copy, revisit, all_paths)


def load_data():
    global graph, small_caves

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

        # Remember the small caves (used in part 2)
        if endpoints[0] == endpoints[0].lower():
            small_caves.add(endpoints[0])

        if endpoints[1] == endpoints[1].lower():
            small_caves.add(endpoints[1])

    # Remove the start/end caves from the set
    small_caves.remove('start')
    small_caves.remove('end')

    # print(small_caves)
    # print(graph)


def part1():
    all_paths = set()
    visited = set()
    visited.add('start')
    find_paths('start', visited, ['start'], None, all_paths)

    # for path in all_paths:
    #     print(path)

    print('Part 1: ' + str(len(all_paths)))


def part2():
    all_paths = set()
    for small_cave in small_caves:
        visited = set()
        visited.add('start')
        find_paths('start', visited, ['start'], small_cave, all_paths)

    # for path in all_paths:
    #     print(path)

    print('Part 2: ' + str(len(all_paths)))


load_data()
part1()
part2()