from collections import deque


with open("input.txt", "r") as file:
    INPUT = [l.split(',') for l in file.read().split("\n")]


def part1(part=1, space=None, idx=1024):
    if not space:
        space = [['.' for _ in range(71)] for __ in range(71)]
        for c, r in INPUT[:idx]:
            space[int(r)][int(c)] = '#'

    seen = set()
    q = deque([((0,0), 0)])
    while q:
        coords, steps = q.popleft()
        row, col = coords
        if (row, col) in seen or not 0<=row<=70 or not 0<=col<=70 or space[row][col]=='#':
            continue
        seen.add((row, col))

        if coords == (70,70):
            if part==2:
                return steps, seen, space, [(int(y), int(x)) for x,y in INPUT[idx:][::-1]]
            return steps

        for d_r, d_c in [(-1,0),(1,0),(0,-1),(0,1)]:
            q.append(((row+d_r, col+d_c), steps+1))

    return None

def part2():
    space, idx = None, 1024

    while True:
        _, seen, space, rem = part1(part=2, space=space, idx=idx)
        while rem:
            row, col = rem.pop()
            space[row][col] = '#'
            idx += 1
            if (row, col) in seen:
                if part1(part=2, space=space, idx=idx) == None:
                    return (row, col)
                break

    return INPUT[-1]


if __name__=='__main__':
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")