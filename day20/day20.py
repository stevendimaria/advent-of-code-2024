from collections import deque
from tqdm import tqdm

with open("input.txt", "r") as file:
    MAP = file.read().split("\n")
START, END = None, None
for i in range(len(MAP)):
    for j in range(len(MAP[0])):
        if MAP[i][j]=='S':
            START = (i,j)
        elif MAP[i][j]=='E':
            END = (i,j)
        else:
            continue


def get_steps_to_end():
    steps_to_end, cheats = {}, set()
    q = deque([(END, 0)])
    while q:
        coords, steps = q.popleft()
        if coords in steps_to_end:
            continue
        steps_to_end[coords] = steps

        row,col = coords
        for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0<=r+row<len(MAP) and 0<=c+col<len(MAP[0]):
                if MAP[r + row][c + col] != '#':
                    q.append(((r+row,c+col), steps+1))
                else:
                    cheats.add(((row,col),(r+row,c+col)))
    return steps_to_end, cheats


def get_mnhtn_dist(start,steps_to_end,tgt):
    row, col = start
    possible = set()
    for i in range(21):
        for j in range(21):
            if 2<=i+j<=20:
                for r,c in [(i,j),(i,j*-1),(i*-1,j),(i*-1,j*-1)]:
                    if 0<=row+r<len(MAP) and 0<=col+c<len(MAP[0]) and MAP[row+r][col+c]!='#' and abs(steps_to_end[start]-steps_to_end[(row+r,col+c)])>=tgt:
                        possible.add((row+r,col+c))
    return possible


def part1():
    ans = 0
    steps_to_end, cheats = get_steps_to_end()
    while cheats:
        good, cheat = cheats.pop()
        cr,cc = cheat
        for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0<cr+r<len(MAP)-1 and 0<cc+c<len(MAP[0]) and (cr+r,cc+c)!=good and MAP[cr+r][cc+c]!='#':
                n = steps_to_end[good]-steps_to_end[(cr+r,cc+c)]-2
                if n>=100:
                    ans += 1
    return ans



def part2(tgt=100):
    cheat_list = {}
    steps_to_end, cheats = get_steps_to_end()

    for k in tqdm(steps_to_end):
        if steps_to_end[k]<=tgt or not (possible := get_mnhtn_dist(k, steps_to_end, tgt)):
            continue

        q = deque([(k,0)])
        seen = set()
        while q:
            curr, steps = q.popleft()
            if steps>20 or (curr,steps) in seen:
                continue

            if curr in possible:
                n = (steps_to_end[k] - steps_to_end[curr]) - steps
                if n<tgt:
                    continue
                if not cheat_list.get((k,curr)):
                    cheat_list[(k,curr)] = set()

                cheat_list[(k, curr)].add(n)
                possible -= {curr}

            row, col = curr
            for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= r + row < len(MAP) and 0 <= c + col < len(MAP[0]):
                    q.append(((row+r,col+c), steps+1))
            seen.add((curr, steps))

    ans, tmp = 0, {}
    for k,v in cheat_list.items():
        ans += len(v)
    return ans
