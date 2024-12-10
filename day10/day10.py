from collections import deque

with open("input.txt") as file:
    TOPO_MAP = [line.rstrip() for line in file]

STARTS = []
for r in range(len(TOPO_MAP)):
    for c in range(len(TOPO_MAP[0])):
        if TOPO_MAP[r][c] == "0":
            STARTS.append((r, c))


def part1(part2=False):
    part1_ans = 0
    part2_ans = 0
    for row, col in STARTS:
        tot = set()
        q = deque([((row, col), 0)])
        while q:
            coords, curr = q.popleft()
            if curr == 9:
                tot.add(coords)
                if part2:
                    part2_ans += 1
                continue
            r, c = coords

            for _r, _c in [(r - 1, c),(r + 1, c),(r, c - 1),(r, c + 1)]:
                if not 0 <=_r< len(TOPO_MAP) or not 0 <=_c< len(TOPO_MAP[0]):
                    continue
                if (i := int(TOPO_MAP[_r][_c])) - curr == 1:
                    q.append(((_r, _c), i))
        part1_ans += len(tot)
    return part1_ans, part2_ans


if __name__ == "__main__":
    print(f"Part 1 : {part1()[0]}")
    print(f"Part 2 : {part1(True)[1]}")
