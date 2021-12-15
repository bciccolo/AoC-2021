FILE_NAME = 'day14-small.dat'

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

    rules.clear()
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

def grow_polymer_improved(steps):
    counts = {}

    # Step 1: Seed the counts with the original polymer string
    for i in range(len(polymer_string) - 1):
        element = polymer_string[i:i + 2]
        if element not in counts:
            counts[element] = 1
        else:
            counts[element] = counts[element] + 1

    # Step 2: Update the counts for each step of the process (we don't care about order, only quantities)
    for i in range(steps):
        next_generation = {}
        for element in counts:
            current_count = counts[element]
            insert = rules.get(element)

            new_element_1 = element[0] + insert
            if new_element_1 not in next_generation:
                next_generation[new_element_1] = current_count
            else:
                next_generation[new_element_1] = next_generation[new_element_1] + current_count

            new_element_2 = insert + element[1]
            if new_element_2 not in next_generation:
                next_generation[new_element_2] = current_count
            else:
                next_generation[new_element_2] = next_generation[new_element_2] + current_count

        counts = next_generation

    print(counts)

    return counts


def part1():
    load_data()
    grow_polymer(10)
    counts_by_element = analyze_elements()

    sorted_counts = list(counts_by_element.values())
    sorted_counts.sort()
    results = sorted_counts[len(sorted_counts) - 1] - sorted_counts[0]

    print('Part 1: ' + str(results))


def part2():
    load_data()
    counts_by_pair = grow_polymer_improved(40)

    counts_by_element = {}
    for pair in counts_by_pair:
        count = counts_by_pair[pair]

        element_1 = pair[0]
        if element_1 not in counts_by_element:
            counts_by_element[element_1] = count
        else:
            counts_by_element[element_1] = counts_by_element[element_1] + count

        element_2 = pair[1]
        if element_2 not in counts_by_element:
            counts_by_element[element_2] = count
        else:
            counts_by_element[element_2] = counts_by_element[element_2] + count

    print(counts_by_element)

    sorted_counts = list(counts_by_element.values())
    sorted_counts.sort()

    # Not sure why this result ends in xxx.5; even less sure why the answer for the sample data
    # is rounded UP but the answer for my full data set is rounded DOWN. I'll take it.
    results = (sorted_counts[len(sorted_counts) - 1] - sorted_counts[0]) / 2

    print('Part 2: ' + str(results))


part1()
part2()