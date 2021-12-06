FILE_NAME = 'day4.dat'
MARKED = -1

boards = []  # The list of Bingo boards that are available
numbers = [] # The list of Bingo numbers that are called


def calculate_score(board):
    score = 0

    for row in board:
        for col in row:
            if col != MARKED:
                score = score + col

    return score

def check_winner(board):
    # Check rows
    for row in board:
        if (row[0] == MARKED and
            row[1] == MARKED and
            row[2] == MARKED and
            row[3] == MARKED and
            row[4] == MARKED):
            return True

    # Check columns
    for i in range(len(board[0])):
        if (board[0][i] == MARKED and
            board[1][i] == MARKED and
            board[2][i] == MARKED and
            board[3][i] == MARKED and
            board[4][i] == MARKED):
            return True

    # No winner found, return false
    return False


def load_data():
    global boards, numbers

    file = open(FILE_NAME, 'r')
    lines = file.readlines()

    # The first line is the list of numbers
    numbers = [int(number) for number in lines[0].strip().split(',')]

    # The rest of the file represents the boards (5 lines for the board, 1 blank line)
    for i in range(2, len(lines), 6):
        board = []
        board.append([int(number) for number in lines[i    ].strip().split()])
        board.append([int(number) for number in lines[i + 1].strip().split()])
        board.append([int(number) for number in lines[i + 2].strip().split()])
        board.append([int(number) for number in lines[i + 3].strip().split()])
        board.append([int(number) for number in lines[i + 4].strip().split()])

        boards.append(board)

    # Test results
    # print(numbers)
    # print('board 1:')
    # print(boards[1])
    # print('board 2:')
    # print(boards[2])


def update_board(board, number):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == number:
                board[row][col] = MARKED


def part1():
    global boards, numbers

    load_data()

    for number in numbers:
        for i in range(len(boards)):
            update_board(boards[i], number)
            if check_winner(boards[i]):
                score = calculate_score(boards[i])
                final = score * number;
                print(i)
                print(boards[i])
                print(score)
                print(number)
                print('Part 1: ' + str(final))
                return


part1()