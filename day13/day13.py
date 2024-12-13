from itertools import groupby
from tqdm import tqdm
with open("input.txt", "r") as file:
    INPUT = file.read().split("\n")
temp_games = []
for key, group in groupby(INPUT, lambda x: x != ""):
    if key:
        temp_games.append(list(group))

GAMES = []
for i, _game in enumerate(temp_games):
    button_a = _game[0].split("A: ")[1].split("+")
    button_a = tuple([int(button_a[1].split(",")[0]), int(button_a[2])])

    button_b = _game[1].split("B: ")[1].split("+")
    button_b = tuple([int(button_b[1].split(",")[0]), int(button_b[2])])

    prize = _game[2].split("Prize: ")[1].split("=")
    prize = tuple([int(prize[1].split(",")[0]), int(prize[2])])

    GAMES.append([button_a, button_b, prize])


def part1(game):
    x_eq = (game[0][0], game[1][0], game[2][0])
    y_eq = (game[0][1], game[1][1], game[2][1])
    det = (x_eq[0] * y_eq[1]) - (x_eq[1] * y_eq[0])

    inv = [[y_eq[1], -x_eq[1]], [-y_eq[0], x_eq[0]]]

    x_ans, x_rem = divmod(((inv[0][0] * x_eq[2]) + (inv[0][1] * y_eq[2])), det)
    y_ans, y_rem = divmod(((inv[1][0] * x_eq[2]) + (inv[1][1] * y_eq[2])), det)
    if x_ans >= 0 == x_rem == y_rem <= y_ans:
        return (3 * x_ans) + y_ans
    return 0

    # ===================================================================
    # Queue is maybe more intuitive but won't scale

    # ans, seen = 0, set()
    # q = deque([(0, 0, 0)])  # x, y, presses
    # while q:
    #     x, y, p = q.popleft()
    #     target = game[2]
    #     if (x, y) == target:
    #         ans += p
    #         break
    #     if ((x,y,p) in seen) or (x>target[0] or y>target[1]):
    #         continue
    #     seen.add((x,y,p))
    #
    #     q.append((x+game[0][0], y+game[0][1], p+3))
    #     q.append((x+game[1][0], y+game[1][1], p+1))
    #
    # return ans
    # ===================================================================


def part2():
    ans = 0
    for g in GAMES:
        ans += part1([g[0], g[1], (g[2][0] + 10000000000000, g[2][1] + 10000000000000)])

    return ans


if __name__ == "__main__":
    part1_ans = 0
    for game in tqdm(GAMES):
        part1_ans += part1(game)
    print(f"Part 1 : {part1_ans}")
    print(f"Part 2 : {part2()}")