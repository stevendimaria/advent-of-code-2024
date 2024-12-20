from collections import deque
from heapq import heappush, heappop

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
            if 0<r+row<len(MAP)-1 and 0<c+col<len(MAP[0])-1:
                if MAP[r + row][c + col] != '#':
                    q.append(((r+row,c+col), steps+1))
                else:
                    cheats.add(((row,col),(r+row,c+col)))
    return steps_to_end, cheats



def part1():
    ans = 0
    # temp_ct = {}
    steps_to_end, cheats = get_steps_to_end(*END)
    while cheats:
        good, cheat = cheats.pop()
        cr,cc = cheat
        for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0<cr+r<len(MAP)-1 and 0<cc+c<len(MAP[0]) and (cr+r,cc+c)!=good and MAP[cr+r][cc+c]!='#':
                n = steps_to_end[good]-steps_to_end[(cr+r,cc+c)]-2
                if n>=100:
                    # temp_ct[n] = temp_ct.get(n,0) + 1
                    ans += 1
    # print({k: v for k, v in sorted(temp_ct.items(), key=lambda item: item[0])})
    return ans



def part2():
    pass


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")

