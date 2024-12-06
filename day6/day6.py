with open("input.txt") as file:
    MAP = [line.rstrip() for line in file]
ROW_LEN = len(MAP)
COL_LEN = len(MAP[0])


def part1():
    guard_row, guard_col = None, None
    guard_dir = None
    barriers = set()
    next_dirs = {"^": ">", ">": "v", "v": "<", "<": "^"}
    ans = set()

    for r, row in enumerate(MAP):
        for c, col in enumerate(row):
            if col == "#":
                barriers.add((r, c))
            elif col in {"^", "v", "<", ">"}:
                guard_dir = col
                guard_row = r
                guard_col = c
            else:
                continue

    while 0 <= guard_row < ROW_LEN and 0 <= guard_col < COL_LEN:
        ans.add((guard_row, guard_col))

        gr, gc = guard_row, guard_col
        if guard_dir == "^":
            gr -= 1
        elif guard_dir == "v":
            gr += 1
        elif guard_dir == "<":
            gc -= 1
        else:
            gc += 1

        if MAP[gr][gc] == "#":
            guard_dir = next_dirs[guard_dir]
        else:
            guard_row, guard_col = gr, gc

    return len(ans)


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
#     print(f"Part 2 : {part2()}")
