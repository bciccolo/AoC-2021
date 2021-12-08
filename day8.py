FILE_NAME = 'day8-small.dat'

def part1():
    count = 0

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    for line in lines:
        digits = line.strip().split('|')[1].split()
        unique_digits = [digit for digit in digits if len(digit) == 2 or len(digit) == 3 or len(digit) ==  4 or len(digit) ==  7]
        count = count + len(unique_digits)

    print('Part 1: ' + str(count))


def part2():
    pass


part1()
part2()