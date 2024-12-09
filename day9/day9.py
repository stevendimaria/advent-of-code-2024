with open("input.txt") as file:
    DISKMAP = [line.rstrip() for line in file][0]


def part1():
    full, empty = {}, {}
    for i, n in enumerate(DISKMAP):
        if not i % 2:
            full[i // 2] = int(n)
        else:
            empty[i // 2] = int(n)

    space_map = []
    for k in full:
        space_map.extend(
            [str(k) for _ in range(full.get(k, 0))]
            + ["" for _ in range(empty.get(k, 0))]
        )

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


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
