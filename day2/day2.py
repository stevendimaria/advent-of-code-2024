with open('input.txt') as file:
    REPORTS = [[int(n) for n in line.rstrip().split()] for line in file]


def part1(report: list):
    if report in [sorted(report), sorted(report, reverse=True)]:
        diff = [abs(report[i - 1] - report[i]) for i in range(1, len(report))]
    else:
        return 0

    return 1 if min(diff) >= 1 and max(diff) <= 3 else 0


def part2(report: list):
    if part1(report[1:]) or part1(report[:-1]):
        return 1

    if report[0] < report[1]:
        how = 'asc'
    elif report[0] > report[1]:
        how = 'desc'
    else:
        return 0

    for i in range(1, len(report)):
        if how == 'asc' and 1 <= report[i] - report[i - 1] <= 3:
            continue
        elif how == 'desc' and 1 <= report[i - 1] - report[i] <= 3:
            continue
        else:
            return max(
                part1(report[:i - 1] + report[i:]),
                part1(report[:i] + report[i + 1:])
            )
    return 1


if __name__ == '__main__':
    part_1_ans = 0
    part_2_ans = 0

    for _report in REPORTS:
        part_1_ans += (_p1 := part1(_report))
        if _p1 or part2(_report):
            part_2_ans += 1

    print(f'Part 1 : {part_1_ans}')
    print(f'Part 2 : {part_2_ans}')
