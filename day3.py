DIGITS = 12

def part1():
    # Intialize two counter arrays to keep track of the 1s and 0s
    one_counts = []
    zero_counts = []
    for i in range(DIGITS):
        one_counts.append(0)
        zero_counts.append(0)

    # Parse each binary number in the file and update the counter arrays
    file = open('day3.dat', 'r')
    lines = file.readlines()

    for line in lines:
        binary = line.strip()
        index = 0
        for digit in binary:
            if digit == '1':
                one_counts[index] = one_counts[index] + 1
            else:
                zero_counts[index] = zero_counts[index] + 1
            index = index + 1

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
    print("Part 1: " + str(product))


part1()