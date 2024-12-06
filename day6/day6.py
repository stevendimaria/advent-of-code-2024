with open("input.txt") as file:
    MAP = [line.rstrip() for line in file]
ROW_LEN = len(MAP)
COL_LEN = len(MAP[0])

def part1():
    guard_row, guard_col = None, None
    guard_dir = None
    barriers, clear = set(), {'.',"^", ">", "v","<"}
    next_dirs = {"^": ">", ">": "v", "v": "<", "<": "^"}
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
                start = [col, r,c]
            else:
                continue

    while 0 <= guard_row < ROW_LEN and 0 <= guard_col < COL_LEN:
        ans.add(((guard_row, guard_col), guard_dir))

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

    return ans, start

def part2(candidates: set):
    next_barrier = {}
    for r in range(ROW_LEN):
        for c in range(COL_LEN):
            if MAP[r][c]=='#' or next_barrier.get((r,c)):
                continue

            for rd in range(r, ROW_LEN):
                if MAP[rd][c] == '#':
                    for _rd in range(r, rd):
                        if not next_barrier.get((_rd,c)):
                            next_barrier[(_rd,c)] = {}
                        next_barrier[(_rd,c)]['v'] = (rd,c)
                    break
            for ru in range(r, -1, -1):
                if MAP[ru][c] == '#':
                    for _ru in range(r, ru, -1):
                        if not next_barrier.get((_ru,c)):
                            next_barrier[(_ru,c)] = {}
                        next_barrier[(_ru,c)]['^'] = (ru,c)
                    break
            for cr in range(c, COL_LEN):
                if MAP[r][cr] == '#':
                    for _cr in range(c, cr):
                        if not next_barrier.get((r, _cr)):
                            next_barrier[(r, _cr)] = {}
                        next_barrier[(r, _cr)]['>'] = (cr, c)
                    break
            for cl in range(c, -1, -1):
                if MAP[r][cl] == '#':
                    for _cl in range(c, cl, -1):
                        if not next_barrier.get((r, _cl)):
                            next_barrier[(r, _cl)] = {}
                        next_barrier[(r, _cl)]['<'] = (cl, c)
                    break
    # print(next_barrier)
    ans = set()
    while candidates:
        coords, g_dir = candidates.pop()
        r,c = coords
        seen = set()
        if g_dir == '^'  and r>0 and MAP[r-1][c]!='#':
            seen.add((r-1,c))
            g_dir = '>'
        elif g_dir == 'v' and r<ROW_LEN-1 and MAP[r+1][c]!='#':
            g_dir = '<'
            seen.add((r+1, c))
        elif g_dir == '<' and c>0 and MAP[r][c-1]!='#':
            g_dir = '^'
            seen.add((r, c-1))
        elif g_dir == '>' and c < COL_LEN - 1 and MAP[r][c + 1] != '#':
            g_dir = 'v'
            seen.add((r,c+1))
        else:
            continue
        box_test = False
        while not box_test:
            print(seen, g_dir, (r,c), next_barrier.get((r,c)))

            if g_dir == '>' and next_barrier.get((r,c)) and next_barrier[(r,c)].get('>'):
                print(g_dir, (r,c), next_barrier[(r, c)])
                _nxt = next_barrier[(r, c)]['>']
                if _nxt in seen:
                    box_test = True
                    break

                _r = next_barrier[(r,c)]['>'][0]
                _c = next_barrier[(r, c)]['>'][1]-1
                r,c = _r,_c
                seen.add(_nxt)
            elif g_dir=='v' and next_barrier.get((r,c)) and next_barrier[(r,c)].get('v'):
                print(g_dir, (r, c), next_barrier[(r, c)])
                _nxt = next_barrier[(r, c)]['v']
                if _nxt in seen:
                    box_test = True
                    break

                _r = next_barrier[(r,c)]['v'][0]-1
                _c = next_barrier[(r, c)]['v'][1]
                r, c = _r, _c
                seen.add(_nxt)

            elif g_dir=='^' and next_barrier.get((r,c)) and next_barrier[(r,c)].get('^'):
                print(g_dir, (r, c), next_barrier[(r, c)])
                _nxt = next_barrier[(r, c)]['^']
                if _nxt in seen:
                    box_test = True
                    break

                _r = next_barrier[(r,c)]['^'][0]+1
                _c = next_barrier[(r, c)]['^'][1]
                r, c = _r, _c
                seen.add(_nxt)

            elif g_dir=='<' and next_barrier.get((r,c)) and next_barrier[(r,c)].get('<'):
                print(g_dir, (r, c), next_barrier[(r, c)])
                _nxt = next_barrier[(r, c)]['<']
                if _nxt in seen:
                    box_test = True
                    break

                _r = next_barrier[(r,c)]['<'][0]
                _c = next_barrier[(r, c)]['<'][1]+1
                r, c = _r, _c
                seen.add(_nxt)

            else:
                break

        if box_test:
            ans.add(coords)

    return ans

if __name__ == "__main__":
    _candidates, _start = part1()

    part1_ans = set()
    for coord, _ in _candidates:
        part1_ans.add(coord)
    print(f"Part 1 : {len(part1_ans)}")
    print(f"Part 2 : {len(part2(_candidates))}")
