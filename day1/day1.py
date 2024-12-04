from heapq import heappop, heappush

with open("input.txt") as file:
    LOCATIONS = [[int(n) for n in line.rstrip().split()] for line in file]


def part1():
    h1, h2 = [], []
    for loc1, loc2 in LOCATIONS:
        heappush(h1, loc1)
        heappush(h2, loc2)

    tot = 0
    while h1 and h2:
        tot += abs(heappop(h1) - heappop(h2))

    return tot


def part2():
    r_track, l_track = {}, {}
    for loc1, loc2 in LOCATIONS:
        if not r_track.get(loc1):
            r_track[loc1] = 0

        r_track[loc1] += 1
        l_track[loc2] = l_track.get(loc2, 0) + 1

    tot = 0
    for k, v in r_track.items():
        if l := l_track.get(k):
            tot += k * v * l

    return tot


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")
