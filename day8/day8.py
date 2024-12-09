with open("input.txt") as file:
    MAP = [line.rstrip() for line in file]

LOCATIONS = {}
ROWS = len(MAP)
COLS = len(MAP[0])
for r in range(len(MAP)):
    for c in range(len(MAP[0])):
        if MAP[r][c] == ".":
            continue

        if not LOCATIONS.get((ch := MAP[r][c])):
            LOCATIONS[ch] = []
        LOCATIONS[ch].append((r, c))


def part1(part2=False):
    antinodes = set()
    for _, locs in LOCATIONS.items():
        for i in range(len(locs)):
            for j in range(len(locs)):
                if i == j:
                    continue

                diff = (locs[i][0] - locs[j][0], locs[i][1] - locs[j][1])
                if not part2:
                    an = (locs[i][0] + diff[0]), (locs[i][1] + diff[1])
                    if 0 <= an[0] < ROWS and 0 <= an[1] < COLS:
                        antinodes.add(an)
                else:
                    an = ((locs[i][0]), (locs[i][1]))
                    while 0 <= an[0] < ROWS and 0 <= an[1] < COLS:
                        antinodes.add(an)
                        an = (an[0] + diff[0], an[1] + diff[1])

                    an = (locs[i][0]), (locs[i][1])
                    while 0 <= an[0] < ROWS and 0 <= an[1] < COLS:
                        antinodes.add(an)
                        an = (an[0] - diff[0], an[1] - diff[1])
    return len(antinodes)


def part2():
    return part1(part2=True)


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")
