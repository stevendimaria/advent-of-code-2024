import re

CHARS = ''
with open('input.txt') as file:
    for line in file:
        CHARS += line


def part1():
    calcs = re.findall(r"mul\([0-9]+,[0-9]+\)", CHARS)

    ans = 0
    for calc in calcs:
        first, second = calc.split(',')
        first = int(first.split('(')[1])
        second = int(second[:-1])
        ans += first*second

    return ans


if __name__=='__main__':

    print(f'Part 1 : {part1()}')
    # print(f'Part 2 : {part_2_ans}')