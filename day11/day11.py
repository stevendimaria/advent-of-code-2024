from functools import cache
from tqdm import tqdm


with open("input.txt") as file:
    STONES = [int(i) for i in [line.rstrip() for line in file][0].split()]


def reduce(n: int):
    shortcuts = []
    stones = [n]
    steps = 0
    while True:
        ct, _nxt = 0, []
        for stone in stones:
            if stone == 0:
                _nxt.append(1)
                ct += 1
            elif not (_l := len(str(stone))) % 2:
                next_two = [int(str(stone)[: _l // 2]), int(str(stone)[_l // 2 :])]
                _nxt.extend(next_two)
                if max(next_two) < 10:
                    ct += 2
            else:
                _nxt.append(stone * 2024)
        stones = _nxt
        steps += 1
        shortcuts.append((steps, _nxt))
        if steps == 10:
            break
    return {n: sorted(shortcuts, reverse=True)}


def part1(n: int):
    stones = [s for s in STONES]
    for _ in tqdm(range(n)):
        _nxt = []
        for stone in stones:
            if stone == 0:
                _nxt.append(1)
            elif not (_l := len(str(stone))) % 2:
                _nxt.extend([int(str(stone)[: _l // 2]), int(str(stone)[_l // 2 :])])
            else:
                _nxt.append(stone * 2024)
        stones = _nxt
    return len(stones)


@cache
def part2(stone, steps):
    if steps == 75:
        return 1
    if stone == "0":
        return part2("1", steps + 1)
    if len(stone) % 2 == 0:
        left = stone[: int(len(stone) / 2)]
        right = str(int(stone[int(len(stone) / 2) :]))
        return part2(left, steps + 1) + part2(right, steps + 1)
    return part2(str(int(stone) * 2024), steps + 1)


if __name__ == "__main__":
    print(f"Part 1 : {part1(25)}")

    num_stones = 0
    for stone in STONES:
        num_stones += part2(str(stone), 0)

    print("Part 2:", num_stones)
