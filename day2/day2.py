with open('input.txt') as file:
    REPORTS = [[int(n) for n in line.rstrip().split()] for line in file]


def part1():
    safe = 0

    for report in REPORTS:
        if report == sorted(report):
            diff = [report[i] - report[i - 1] for i in range(1, len(report))]
            if min(diff) >= 1 and max(diff) <= 3:
                safe += 1
        elif report == sorted(report, reverse=True):
            diff = [report[i - 1] - report[i] for i in range(1, len(report))]
            if min(diff) >= 1 and max(diff) <= 3:
                safe += 1
        else:
            pass

    return safe

def part2():
    pass


if __name__ == '__main__':
    print(f'Part 1 : {part1()}')
