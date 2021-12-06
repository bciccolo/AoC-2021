DIGITS = 12
FILE_NAME = 'day3.dat'

one_counts = []
zero_counts = []


def analyze_digits(numbers):
    global one_counts, zero_counts

    # Reset the counter arrays because this function can be call multiple times
    one_counts.clear()
    zero_counts.clear()

    # Intialize two counter arrays to keep track of the 1s and 0s
    for i in range(DIGITS):
        one_counts.append(0)
        zero_counts.append(0)

    # Parse each binary number in the file and update the counter arrays
    file = open('day3-small.dat', 'r')
    lines = file.readlines()

    for number in numbers:
        index = 0
        for digit in number:
            if digit == '1':
                one_counts[index] = one_counts[index] + 1
            else:
                zero_counts[index] = zero_counts[index] + 1
            index = index + 1


def get_rating(type):
    # Load all the binary numbers and analyze them...
    numbers = load_numbers()

    # ...we will eliminate elements until only one remains
    # Check the entries to see if the leading digits match the most popular bits
    match = ''
    index = 0
    while (len(numbers) > 1):
        # Analyze the remaining numbers
        analyze_digits(numbers)

        if (type == 'OX' and one_counts[index] >= zero_counts[index]) or (type == 'CO2' and one_counts[index] < zero_counts[index]):
            match = match + '1'
        else:
            match = match + '0'

        # Remove any non-matches
        numbers = [number for number in numbers if number.startswith(match)]
        # print('Loop ' + str(index) + ': ')
        # print(numbers)

        index = index + 1

    # Convert the last remaining number from binary to decimal
    number = numbers[0]
    decimal = 0
    for i in range(DIGITS):
        if number[i] == '1':
            decimal = decimal + pow(2, DIGITS - i - 1)

    return decimal


def load_numbers():
    numbers = []

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    for line in lines:
        numbers.append(line.strip())

    return numbers


def part1():
    numbers = load_numbers()
    analyze_digits(numbers)

    # Compare the counts to calculate the gamma and epsilon values
    gamma = 0
    epsilon = 0
    for i in range(DIGITS):
        if one_counts[i] > zero_counts[i]:
            gamma = gamma + pow(2, DIGITS - i - 1)
        else:
            epsilon = epsilon + pow(2, DIGITS - i - 1)

    # Calculate the product and print the results
    print(gamma)
    print(epsilon)
    product = gamma * epsilon
    print('Part 1: ' + str(product))


def part2():
    oxygen_generator = get_rating('OX')
    co2_scrubber = get_rating('CO2')
    print(oxygen_generator)
    print(co2_scrubber)
    product = oxygen_generator * co2_scrubber
    print('Part 2: ' + str(product))


part1()
part2()