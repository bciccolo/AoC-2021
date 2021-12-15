FILE_NAME = 'day14.dat'

polymer_string = ''
rules = {}


def analyze_elements():
    counts = {}

    for element in polymer_string:
        if element not in counts:
            counts[element] = 1
        else:
            counts[element] = counts[element] + 1

    return counts

def load_data():
    global polymer_string, rules

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    polymer_string = lines[0].strip()

    for i in range(2, len(lines)):
        parts = lines[i].strip().split(' -> ')
        rules[parts[0]] = parts[1]

    # print(polymer_string)
    # print(rules)


def grow_polymer(steps):
    global polymer_string

    # print('Initial: ' + polymer_string)

    for i in range(steps):
        next_generation = ''

        for j in range(len(polymer_string) - 1):
            element = polymer_string[j:j + 2]
            insert = rules.get(element)
            next_generation = next_generation + element[0] + insert

        next_generation = next_generation + polymer_string[len(polymer_string) - 1]
        polymer_string = next_generation

        # print('Step ' + str(i + 1) + ': ' + polymer_string)


def part1():
    load_data()
    grow_polymer(10)
    counts_by_element = analyze_elements()

    sorted_counts = list(counts_by_element.values())
    sorted_counts.sort()
    results = sorted_counts[len(sorted_counts) - 1] - sorted_counts[0]

    print('Part 1: ' + str(results))


def part2():
    print('Part 2: ' + str(0))


part1()
part2()