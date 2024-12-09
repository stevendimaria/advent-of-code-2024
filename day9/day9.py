from tqdm import tqdm

with open("input.txt") as file:
    DISKMAP = [line.rstrip() for line in file][0]
FULL, EMPTY = {}, {}
for i, n in enumerate(DISKMAP):
    if not i % 2:
        FULL[i // 2] = int(n)
    else:
        EMPTY[i // 2] = int(n)

SPACE_MAP = []
for k in FULL:
    SPACE_MAP.extend(
        [str(k) for _ in range(FULL.get(k, 0))] + ["" for _ in range(EMPTY.get(k, 0))]
    )


def part1():
    space_map = [x for x in SPACE_MAP]

    ans, ptr = [], 0
    while ptr < len(space_map):
        if space_map[ptr]:
            ans.append(int(space_map[ptr]))
            ptr += 1
        else:
            temp = space_map.pop()
            if temp:
                ans.append(int(temp))
                ptr += 1
    return sum([i * n for i, n in enumerate(ans)])


def part2():
    ans = []
    for i, x in enumerate([int(_) for _ in DISKMAP]):
        if x == 0:
            continue
        if not i % 2:
            ans.append((x, i // 2))
        else:
            ans.append((x, -1))

    files = [f for f in ans if f[1] != -1]

    while files:
        x, y = files.pop()
        idx = ans.index((x, y))
        _nxt = []
        for k, (i, j) in enumerate(ans):
            if j == -1 and i >= x and k < idx:
                _nxt = [(k, (x, y)), (k + 1, (i - x, -1)), (idx + 1, (x, -1))]
                break

        if _nxt:
            p, b = _nxt[0]
            p2, b2 = _nxt[1]
            p3, b3 = _nxt[2]
            ans[p] = b
            ans.insert(p2, b2)
            ans[p3] = b3

    tot = 0
    result = []
    for x, y in ans:
        result.extend(x * [y])

    for i, x in enumerate(result):
        if x == -1:
            continue
        tot += i * x

    return tot


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")
