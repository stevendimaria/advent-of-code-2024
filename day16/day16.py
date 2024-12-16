from heapq import heappush, heappop

with open("input.txt", "r") as file:
    MAZE = file.read().split("\n")

MOVESET = {
    "^": {"r": -1, "c": 0},
    "v": {"r": 1, "c": 0},
    ">": {"r": 0, "c": 1},
    "<": {"r": 0, "c": -1},
}
START, END = None, None
for idx_r, row in enumerate(MAZE):
    for idx_c, char in enumerate(row):
        if char == "S":
            START = (idx_r, idx_c)
        elif char == "E":
            END = (idx_r, idx_c)
        else:
            continue
    if START and END:
        break


def part1():
    pq = []
    heappush(pq, (0, START[0], START[1], ">"))

    seen, ans = set(), 9999999999
    while pq:
        score, r, c, d = heappop(pq)

        if (r, c, d) in seen:
            continue
        seen.add((r, c, d))

        if MAZE[r][c] == "#" or score >= ans:
            continue
        if (r, c) == END:
            return score

        heappush(pq, (score + 1, r + MOVESET[d]["r"], c + MOVESET[d]["c"], d))

        if d in {"^", "v"}:
            heappush(pq, (score + 1000, r, c, ">"))
            heappush(pq, (score + 1000, r, c, "<"))
        if d in {">", "<"}:
            heappush(pq, (score + 1000, r, c, "^"))
            heappush(pq, (score + 1000, r, c, "v"))

    return -1


def part2(part1_ans):
    pq = []
    heappush(pq, (0, START[0], START[1], ">", set()))

    part2_ans, seen, best = set(), {}, 999999999
    while pq:
        score, r, c, d, path = heappop(pq)

        if score > part1_ans:
            break
        if score > best or MAZE[r][c] == "#" or (r, c, d) in path:
            continue
        if score > seen.get((r, c, d), 9999999999):
            continue
        else:
            seen[(r, c, d)] = score

        next_path = path | {(r, c, d)}
        if (r, c) == END:
            best = min(score, best)
            if score == part1_ans:
                part2_ans |= next_path
            continue

        for next_d in ["<", ">", "^", "v"]:
            next_r, next_c = r + MOVESET[next_d]["r"], c + MOVESET[next_d]["c"]
            if (not 0 <= next_r < len(MAZE) or not 0 <= next_c < len(MAZE[0])) or MAZE[
                next_r
            ][next_c] == "#":
                continue

            if d == next_d:
                heappush(pq, (score + 1, next_r, next_c, d, next_path))

            if d in {"^", "v"} and next_d in {">", "<"}:
                heappush(pq, (score + 1001, next_r, next_c, next_d, next_path))
            if d in {">", "<"} and next_d in {"^", "v"}:
                heappush(pq, (score + 1001, next_r, next_c, next_d, next_path))

    coords = set()
    while part2_ans:
        r, c, _ = part2_ans.pop()
        coords.add((r, c))
    return len(coords)


if __name__ == "__main__":
    part1_ans = part1()
    print(f"Part 1 : {part1_ans}")
    print(f"Part 2 : {part2(part1_ans)}")
