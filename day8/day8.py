with open("input.txt") as file:
    MAP = [line.rstrip() for line in file]

LOCATIONS = {}
ROWS = len(MAP)
COLS = len(MAP[0])
for r in range(len(MAP)):
    for c in range(len(MAP[0])):
        if MAP[r][c]=='.':
            continue

        if not LOCATIONS.get((ch := MAP[r][c])):
            LOCATIONS[ch] = []
        LOCATIONS[ch].append((r,c))


def part1():
    antinodes = set()
    for _, locs in LOCATIONS.items():
        # antinodes[k] = {}
        for i in range(len(locs)):
            # antinodes[k][locs[i]] = []
            for j in range(len(locs)):
                if i==j:
                    continue
                an = (locs[i][0]+(locs[i][0]-locs[j][0])), (locs[i][1]+(locs[i][1]-locs[j][1]))
                if 0<=an[0]<ROWS and 0<=an[1]<COLS:
                    antinodes.add(an)
    return len(antinodes)


if __name__=='__main__':
    print(f"Part 1 : {part1()}")
