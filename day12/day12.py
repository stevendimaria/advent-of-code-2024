from collections import deque

with open("input.txt") as file:
    GARDEN = [line.rstrip() for line in file]


def get_plots():
    regions, r_id = {}, 1
    seen = set()
    for r, row in enumerate(GARDEN):
        for c, col in enumerate(row):
            if (r, c) in seen:
                continue

            regions[r_id] = set()
            q = deque([(r, c)])
            while q:
                x, y = q.popleft()
                if (x, y) in seen or GARDEN[x][y] != GARDEN[r][c]:
                    continue

                seen.add((x, y))
                regions[r_id].add((x, y))
                for _r, _c in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= _r < len(GARDEN) and 0 <= _c < len(GARDEN[0]):
                        q.append((_r, _c))
            r_id += 1
    return regions


REGIONS = get_plots()


def part1():
    ans = {}
    for k, v in REGIONS.items():
        ans[k] = {"n_plants": len(v), "perimeter": 0}
        for row, col in list(v):
            ans[k]["perimeter"] += sum(
                [
                    1
                    for r, c in [
                        (row - 1, col),
                        (row + 1, col),
                        (row, col + 1),
                        (row, col - 1),
                    ]
                    if (r, c) not in v
                ]
            )
    return sum([v["n_plants"] * v["perimeter"] for _, v in ans.items()])


def part2():
    ans = {}
    for k, v in REGIONS.items():
        ans[k] = {"n_plants": len(v), "in": {}, "out": set()}
        for row, col in list(v):
            for _r, _c in (
                missing := [
                    (r, c)
                    for r, c in [
                        (row - 1, col),
                        (row + 1, col),
                        (row, col + 1),
                        (row, col - 1),
                    ]
                    if (r, c) not in v
                ]
            ):
                ans[k]["in"][(_r, _c)] = ans[k]["in"].get((_r, _c), -1) + 1

            if len(missing) > 1:
                if (row - 1, col) not in v and (row, col + 1) not in v:
                    ans[k]["out"].add(tuple(sorted([(row - 1, col), (row, col + 1)])))
                if (row + 1, col) not in v and (row, col + 1) not in v:
                    ans[k]["out"].add(tuple(sorted([(row + 1, col), (row, col + 1)])))
                if (row - 1, col) not in v and (row, col - 1) not in v:
                    ans[k]["out"].add(tuple(sorted([(row - 1, col), (row, col - 1)])))
                if (row + 1, col) not in v and (row, col - 1) not in v:
                    ans[k]["out"].add(tuple(sorted([(row + 1, col), (row, col - 1)])))
    tot = 0
    for _, v in ans.items():
        sides = len(v["out"]) + sum([v["in"][n] for n in v["in"]])
        tot += sides * v["n_plants"]
    return tot


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")
