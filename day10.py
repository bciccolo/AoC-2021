import math

FILE_NAME = 'day10.dat'
OPEN_TOKENS = [ '(', '[', '{', '<' ]

incomplete_entries = []


def part1():
    global incomplete_entries

    # Step 1: Find the corrupt tokens
    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    corrupted_tokens = []
    for line in lines:
        matcher = []

        line = line.strip()

        corrupt = False
        for token in line:
            if token in OPEN_TOKENS:
                matcher.append(token)
            else:
                top = matcher.pop()
                if ((top == '(' and token != ')') or
                    (top == '[' and token != ']') or
                    (top == '{' and token != '}') or
                    (top == '<' and token != '>')):
                    corrupted_tokens.append(token)
                    corrupt = True
                    break

        # This is used in part 2 (really only need the matcher)
        if not corrupt:
            incomplete_entries.append((line, matcher.copy()))

    # print(corrupted_tokens)

    # Step 2: Calculate the "score" of those corrupted tokens
    score = 0
    for token in corrupted_tokens:
        if token == ')':
            score = score + 3
        elif token == ']':
            score = score + 57
        elif token == '}':
            score = score + 1197
        else: # token = '>'
            score = score + 25137

    print('Part 1: ' + str(score))


def part2():
    # Part 2 is unique in that it depends on part 1 being run first!
    scores = []

    for entry in incomplete_entries:
        line = entry[0]
        matcher = entry[1]
        # print(line)
        # print(matcher)

        score = 0

        while len(matcher) > 0:
            token = matcher.pop()

            if token == '(':
                score = score * 5 + 1
            elif token == '[':
                score = score * 5 + 2
            elif token == '{':
                score = score * 5 + 3
            else: # token = '<'
                score = score * 5 + 4

        scores.append(score)

    scores.sort()
    middle = math.floor(len(scores) / 2)

    print('Part 2: ' + str(scores[middle]))


part1()
part2()