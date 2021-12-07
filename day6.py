FILE_NAME = 'day6.dat'
MAX_DAYS = 256

timers_by_day = []


def load_data():
    global timers_by_day

    timers_by_day.clear()

    file = open(FILE_NAME, 'r')
    timers_by_day.append([int(num) for num in file.readlines()[0].strip().split(',')])


def part1():
    load_data()
    simulate()
    # print_daily_timers()
    print('Part 1: ' + str(len(timers_by_day[MAX_DAYS])))


def part2():
    print('Part 2: ' + str(0))


def print_daily_timers():
    for i in range(len(timers_by_day)):
        print('Day ' + str(i) + ': ' + ','.join([str(x) for x in timers_by_day[i]]))


def simulate():
    global timers_by_day

    for i in range(MAX_DAYS):
        print('day ' + str(i) + '...')
        next_day = []
        today = timers_by_day[len(timers_by_day) - 1]
        new = 0
        for timer in today:
            if timer == 0:
                next_day.append(6)
                new = new + 1
            else:
                next_day.append(timer - 1)

        for i in range(new):
            next_day.append(8)

        timers_by_day.append(next_day)

part1()
part2()