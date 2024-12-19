from collections import deque
from tqdm import tqdm


with open("input.txt", "r") as file:
    INPUT = file.read().split("\n")

def part1():
    towels = {}
    for towel in INPUT.pop(0).split(','):
        towel = towel.strip()
        if not towels.get(len(towel)):
            towels[len(towel)] = set()
        towels[len(towel)].add(towel)

    ans = 0
    for pattern in tqdm(INPUT[1:]):
        q = deque([('', pattern)])
        seen = set()
        while q:
            curr, rem = q.popleft()

            if (curr, rem) in seen:
                continue
            seen.add((curr, rem))

            if curr and not towels.get(len(curr)):
                towels[len(curr)] = set()
            if not rem or not set(pattern)-towels.get(1, set()):
                ans += 1
                if curr:
                    towels[len(curr)].add(curr)
                if not towels.get(len(pattern)):
                    towels[len(pattern)] = set()
                towels[len(pattern)].add(pattern)
                break

            for k,v in towels.items():
                if rem[:k] in v:
                    q.append((curr+rem[:k], rem[k:]))

            if curr:
                towels[len(curr)].add(curr)
    return ans


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    # print(f"Part 2 : {part2()}")