from copy import deepcopy
from tqdm import tqdm

with open("input.txt") as file:
    MAP = [line.rstrip() for line in file]
ROW_LEN = len(MAP)
COL_LEN = len(MAP[0])
NEXT_DIRS = {"^": ">", ">": "v", "v": "<", "<": "^"}


def part1():
    guard_row, guard_col = None, None
    guard_dir = None
    barriers, clear = set(), {".", "^", ">", "v", "<"}
    ans = set()
    start = []

    for r, row in enumerate(MAP):
        for c, col in enumerate(row):
            if col == "#":
                barriers.add((r, c))
            elif col in {"^", "v", "<", ">"}:
                guard_dir = col
                guard_row = r
                guard_col = c
                start = [col, r, c]
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
            guard_dir = NEXT_DIRS[guard_dir]
        else:
            guard_row, guard_col = gr, gc

    return ans, start


def part2(start: list, candidates: set):
    part2_ans = set()
    for r, c in tqdm(list(candidates)):
        _map = deepcopy(MAP)
        _map[r] = _map[r][:c] + "#" + _map[r][c + 1 :]

        seen = {}
        _guard_dir, _guard_row, _guard_col = start
        while 0 <= _guard_row < ROW_LEN and 0 <= _guard_col < COL_LEN:
            if not seen.get((_guard_row, _guard_col, _guard_dir)):
                seen[(_guard_row, _guard_col, _guard_dir)] = 0
            elif seen.get((_guard_row, _guard_col, _guard_dir)) > 1:
                part2_ans.add((r, c))
                break
            else:
                pass

            seen[(_guard_row, _guard_col, _guard_dir)] += 1
            _gr, _gc = _guard_row, _guard_col
            if _guard_dir == "^":
                _gr -= 1
            elif _guard_dir == "v":
                _gr += 1
            elif _guard_dir == "<":
                _gc -= 1
            else:
                _gc += 1

            if not 0 <= _gr < ROW_LEN or not 0 <= _gc < COL_LEN:
                break
            elif _map[_gr][_gc] == "#":
                _guard_dir = NEXT_DIRS[_guard_dir]
            else:
                _guard_row, _guard_col = _gr, _gc
        del _map

    return part2_ans


if __name__ == "__main__":
    part1_ans, _start = part1()

    print(f"Part 1 : {len(part1_ans)}")
    print(f"Part 2 : {len(part2(_start, part1_ans))}")
