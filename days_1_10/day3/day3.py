import re

PATTERN = r"mul\([0-9]+,[0-9]+\)"
CHARS = ""
with open("input.txt") as file:
    for line in file:
        CHARS += line


def part1(find_chars: bool = True, calc: str = None):
    if find_chars:
        calcs = re.findall(PATTERN, CHARS)
    else:
        calcs = [calc]

    ans = 0
    for calc in calcs:
        first, second = calc.split(",")
        first = int(first.split("(")[1])
        second = int(second[:-1])
        ans += first * second

    return ans


def part2():
    triggers = CHARS.split("do")
    calcs = []
    for trigger in triggers:
        if trigger.startswith("()"):
            calcs.append("ON")
        if trigger.startswith("n't()"):
            calcs.append("OFF")

        calcs += re.findall(PATTERN, trigger)

    ans, flag = 0, True
    for calc in calcs:
        if calc == "ON":
            flag = True
        elif calc == "OFF":
            flag = False
        elif flag:
            ans += part1(False, calc)
        else:
            continue

    return ans


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")
