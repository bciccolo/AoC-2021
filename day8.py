FILE_NAME = 'day8.dat'


def decode_digits(patterns, digits):
    # Step 1: Identify the segments from the patterns

    # Sort the array by the length of the string for easier access
    patterns.sort(key=len)
    # print(patterns)

    # This array will match each digit to its pattern
    d = [ '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?' ]

    # Unique patterns
    d[1] = patterns[0]
    d[7] = patterns[1]
    d[4] = patterns[2]
    d[8] = patterns[9]

    # The 5-digit pattern (indices 3, 4, or 5) that DOES contain both d1 segments is 3
    d[3] = patterns[3]
    d2or5 = [patterns[4], patterns[5]]
    if d[1][0] in patterns[4] and d[1][1] in patterns[4]:
        d[3] = patterns[4]
        d2or5 = [patterns[3], patterns[5]]
    elif d[1][0] in patterns[5] and d[1][1] in patterns[5]:
        d[3] = patterns[5]
        d2or5 = [patterns[3], patterns[4]]

    # The 6-digit pattern (indices 6, 7, or 8) that does NOT contain both d1 segments is 6
    d[6] = patterns[6]
    d0or9 = [patterns[7], patterns[8]]
    if d[1][0] not in patterns[7] or d[1][1] not in patterns[7]:
        d[6] = patterns[7]
        d0or9 = [patterns[6], patterns[8]]
    elif d[1][0] not in patterns[8] or d[1][1] not in patterns[8]:
        d[6] = patterns[8]
        d0or9 = [patterns[6], patterns[7]]

    # All of d4 is in d9 but NOT d0
    d[0] = d0or9[0]
    d[9] = d0or9[1]
    for letter in d[4]:
        if letter not in d0or9[1]:
            d[0] = d0or9[1]
            d[9] = d0or9[0]
            break

    # The top-right segment from d1 is in d8 but not d6, use that to distinguish d2/d5 (segment NOT in d5)
    top_right = '?'
    for letter in d[8]:
        if letter not in d[6]:
            top_right = letter
            break

    d[2] = d2or5[0] if top_right in d2or5[0] else d2or5[1]
    d[5] = d2or5[1] if top_right in d2or5[0] else d2or5[0]

    # for i in range(10):
    #     print(str(i) + ' = ' + d[i])

    # Now sort the code for each digit for easier comparison
    for i in range(10):
        d[i] = ''.join(sorted(d[i]))

    # for i in range(10):
    #     print(str(i) + ' = ' + d[i])

    # Step 2: Decode the number based on the segments
    number = ''

    for digit in digits:
        # Sort the segments to facilitate comparison
        digit = ''.join(sorted(digit))

        for i in range(10):
            if digit == d[i]:
                number = number + str(i)
                break

    # print(number)

    return int(number)


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
    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    sum = 0

    for line in lines:
        parts = line.strip().split('|')
        patterns = parts[0].split()
        digits = parts[1].split()

        sum = sum + decode_digits(patterns, digits)

    print('Part 2: ' + str(sum))


part1()
part2()