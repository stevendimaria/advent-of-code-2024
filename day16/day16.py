from heapq import heappush, heappop

with open("input.txt", "r") as file:
    MAZE = file.read().split("\n")

MOVESET = {
    "^": {"r": -1, "c": 0},
    "v": {"r": 1, "c": 0},
    ">": {"r": 0, "c": 1},
    "<": {"r": 0, "c": -1},
}


def part1():
    END = None
    h = []
    for r, row in enumerate(MAZE):
        for c, char in enumerate(row):
            if char=='S':
                heappush(h, (0, r, c, '>'))
            elif char=='E':
                END = (r,c)
            else: continue

    seen, ans = set(), 9999999999
    while h:
        score, r, c, d = heappop(h)

        if (r, c, d) in seen:
            continue
        seen.add((r, c, d))
        if MAZE[r][c]=='#' or score>=ans:
            continue

        print(score, r, c, d, MAZE[r][c])
        if (r,c)==END:
            return score
            # ans = min(score, ans)

        heappush(h, (score+1, r+MOVESET[d]['r'], c+MOVESET[d]['c'], d))

        if d in {'^', 'v'}:
            heappush(h, (score+1000, r, c, '>'))
            heappush(h, (score + 1000, r, c, '<'))
        if d in {'>', '<'}:
            heappush(h, (score+1000, r, c, '^'))
            heappush(h, (score + 1000, r, c, 'v'))

    return ans


if __name__=='__main__':
    print(f"Part 1 : {part1()}")
    # print(f"Part 2 : {part2()}")