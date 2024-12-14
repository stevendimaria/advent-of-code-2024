from collections import deque

with open("input.txt") as file:
    INPUT = [line.rstrip() for line in file]
Y_LEN = len(INPUT)
X_LEN = len(INPUT[0])


def letter_search(letter: str, coords: tuple, d: str = ""):
    found = []
    target = {"X": "M", "M": "A", "A": "S"}
    r, c = coords

    if (not d or d == "N") and r > 0 and INPUT[r - 1][c] == target[letter]:
        found.append((target[letter], (r - 1, c), "N"))
    if (not d or d == "S") and r < Y_LEN - 1 and INPUT[r + 1][c] == target[letter]:
        found.append((target[letter], (r + 1, c), "S"))
    if (not d or d == "E") and c < X_LEN - 1 and INPUT[r][c + 1] == target[letter]:
        found.append((target[letter], (r, c + 1), "E"))
    if (not d or d == "W") and c > 0 and INPUT[r][c - 1] == target[letter]:
        found.append((target[letter], (r, c - 1), "W"))

    if (
        (not d or d == "NW")
        and r > 0
        and c > 0
        and INPUT[r - 1][c - 1] == target[letter]
    ):
        found.append((target[letter], (r - 1, c - 1), "NW"))
    if (
        (not d or d == "NE")
        and r > 0
        and c < X_LEN - 1
        and INPUT[r - 1][c + 1] == target[letter]
    ):
        found.append((target[letter], (r - 1, c + 1), "NE"))
    if (
        (not d or d == "SW")
        and c > 0
        and r < Y_LEN - 1
        and INPUT[r + 1][c - 1] == target[letter]
    ):
        found.append((target[letter], (r + 1, c - 1), "SW"))
    if (
        (not d or d == "SE")
        and c < X_LEN - 1
        and r < Y_LEN - 1
        and INPUT[r + 1][c + 1] == target[letter]
    ):
        found.append((target[letter], (r + 1, c + 1), "SE"))

    return found


def part1():
    ans, q = 0, deque([])

    for r, row in enumerate(INPUT):
        for c, ch in enumerate(row):
            if ch == "X":
                q.append(("X", (r, c), ""))
    while q:
        curr, coords, d = q.popleft()
        if curr == "S":
            ans += 1
            continue
        q.extend(letter_search(curr, coords, d))

    return ans


def part2():
    ans = 0
    for r in range(1, Y_LEN - 1):
        for c in range(1, X_LEN - 1):
            if INPUT[r][c] == "A" and set(
                [
                    INPUT[r - 1][c - 1],
                    INPUT[r + 1][c - 1],
                    INPUT[r - 1][c + 1],
                    INPUT[r + 1][c + 1],
                ]
            ) == {"M", "S"}:
                if (
                    INPUT[r - 1][c - 1] != INPUT[r + 1][c + 1]
                    and INPUT[r - 1][c + 1] != INPUT[r + 1][c - 1]
                ):
                    ans += 1
    return ans


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
    print(f"Part 2 : {part2()}")
