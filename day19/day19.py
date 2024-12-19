from collections import deque
from tqdm import tqdm


with open("input.txt", "r") as file:
    INPUT = file.read().split("\n")
TOWELS = INPUT.pop(0)


def part1():
    towels = {}
    for towel in TOWELS.split(","):
        towel = towel.strip()
        if not towels.get(len(towel)):
            towels[len(towel)] = set()
        towels[len(towel)].add(towel)

    ans = 0
    for pattern in INPUT[1:]:
        q = deque([("", pattern)])
        seen = set()
        while q:
            curr, rem = q.popleft()

            if (curr, rem) in seen:
                continue
            seen.add((curr, rem))

            if curr and not towels.get(len(curr)):
                towels[len(curr)] = set()
            if not rem or not set(pattern) - towels.get(1, set()):
                ans += 1
                if curr:
                    towels[len(curr)].add(curr)
                if not towels.get(len(pattern)):
                    towels[len(pattern)] = set()
                towels[len(pattern)].add(pattern)
                break

            for k, v in towels.items():
                if rem[:k] in v:
                    q.append((curr + rem[:k], rem[k:]))

            if curr:
                towels[len(curr)].add(curr)
    return ans


def part2(pattern, cache={}):
    if cache.get(pattern):
        return cache[pattern]
    if not pattern:
        return 1

    ans = 0
    for towel in TOWELS.split(","):
        towel = towel.strip()
        if pattern.startswith(towel):
            ans += part2(pattern[len(towel) :], cache)
    cache[pattern] = ans

    return ans


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")

    tot = 0
    for pattern in tqdm(INPUT[1:]):
        tot += part2(pattern)
    print(f"Part 2 : {tot}")
