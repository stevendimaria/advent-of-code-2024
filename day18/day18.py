from collections import deque


with open("input.txt", "r") as file:
    inp = [l.split(',') for l in file.read().split("\n")]


def part1():
    space = [['.' for _ in range(71)] for __ in range(71)]
    for c, r in inp[:1024]:
        space[int(r)][int(c)] = '#'

    seen = set()
    q = deque([((0,0), 0)])
    while q:
        coords, steps = q.popleft()
        row, col = coords
        if (row, col) in seen or not 0<=row<=70 or not 0<=col<=70 or space[row][col]=='#':
            continue
        elif coords == (70,70):
            return steps
        else:
            seen.add((row,col))

        for d_r, d_c in [(-1,0),(1,0),(0,-1),(0,1)]:
            q.append(((row+d_r, col+d_c), steps+1))

    return None


if __name__=='__main__':
    print(f"Part 1 : {part1()}")