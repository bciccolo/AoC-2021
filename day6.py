FILE_NAME = 'day6.dat'
MAX_DAYS = 80

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
    # Part 2 seems simple: just change MAX_DAYS to 256. Except it won't ever finish - the
    # simulate() algorithm grows exponentially! A new algorithm is needed instead. Rather
    # than tracking each fish independently, we'll group them into age "buckets"
    counts_by_age = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ] # Ages 0-8 days
    file = open(FILE_NAME, 'r')
    for fish in file.readlines()[0].strip().split(','):
        age = int(fish)
        counts_by_age[age] = counts_by_age[age] + 1

    # print(counts_by_age)

    for i in range(256):
        # Rules:
        # 1. Shift every age bucket one spot to the left
        # 2. Bucket 0 goes to buckets 8 AND 6
        age0 = counts_by_age[0]
        for i in range(8):
            counts_by_age[i] = counts_by_age[i + 1]

        counts_by_age[6] = counts_by_age[6] + age0
        counts_by_age[8] = age0

        # print(counts_by_age)

    sum = 0
    for count in counts_by_age:
        sum = sum + count

    print('Part 2: ' + str(sum))


def print_daily_timers():
    for i in range(len(timers_by_day)):
        print('Day ' + str(i) + ': ' + ','.join([str(x) for x in timers_by_day[i]]))


def simulate():
    global timers_by_day

    for i in range(MAX_DAYS):
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