with open("input.txt", "r") as file:
    INPUT = file.read().split()

MAP_1, MAP_2, MOVES = [], [], []
for line in INPUT:
    if line[0] not in {"^", ">", "<", "v"}:
        MAP_1.append([x for x in line])
        MAP_2.append([])
        for ch in MAP_1[-1]:
            if ch in {".", "#"}:
                MAP_2[-1].extend([ch, ch])
            elif ch == "@":
                MAP_2[-1].extend([ch, "."])
            else:
                MAP_2[-1].extend(["[", "]"])
    else:
        MOVES.extend([x for x in line])

MOVESET = {
    "^": {"r": -1, "c": 0},
    "v": {"r": 1, "c": 0},
    ">": {"r": 0, "c": 1},
    "<": {"r": 0, "c": -1},
}


def find_robot(_map):
    for i in range(len(_map)):
        for j in range(len(_map[0])):
            if _map[i][j] == "@":
                return [i, j]
    return None


def day15(_map, part=1):
    for move in MOVES:
        robot = find_robot(_map)
        begin_state, begin_robot = [[_ for _ in _x] for _x in _map], [_ for _ in robot]

        _nxt_r = robot[0] + MOVESET[move]["r"]
        _nxt_c = robot[1] + MOVESET[move]["c"]
        _nxt_char = _map[_nxt_r][_nxt_c]
        if _nxt_char == "#":
            pass
        elif _nxt_char == ".":
            _map[robot[0]][robot[1]], _map[_nxt_r][_nxt_c] = (
                _map[_nxt_r][_nxt_c],
                _map[robot[0]][robot[1]],
            )
        else:
            seen, to_move = set(), []
            _r, _c = robot
            while _map[_r][_c] not in {".", "#"}:
                temp = (_r + MOVESET[move]["r"], _c + MOVESET[move]["c"])
                to_move.append(((_r, _c), temp))
                _r, _c = temp
                seen.add(_map[_r][_c])
            if "." in seen:
                moved = set()
                while to_move:
                    curr, _nxt = to_move.pop()
                    if (curr, _nxt) in moved:
                        continue

                    if part == 2:
                        if "#" in {_map[curr[0]][curr[1]], _map[_nxt[0]][_nxt[1]]}:
                            _map, robot = begin_state, begin_robot
                            break
                        if (brace := _map[curr[0]][curr[1]]) in {"[", "]"} and move in {
                            "^",
                            "v",
                        }:
                            if brace == "[":
                                if _map[_nxt[0]][_nxt[1]] in {"[", "]"}:
                                    if move == "^":
                                        to_move.append((_nxt, (_nxt[0] - 1, _nxt[1])))
                                    else:
                                        to_move.append((_nxt, (_nxt[0] + 1, _nxt[1])))
                                    to_move = [(curr, _nxt)] + to_move
                                    continue
                                else:
                                    to_move.append(
                                        ((curr[0], curr[1] + 1), (_nxt[0], _nxt[1] + 1))
                                    )
                                    moved.add((curr, _nxt))
                            else:
                                if _map[_nxt[0]][_nxt[1]] in {"[", "]"}:
                                    if move == "^":
                                        to_move.append((_nxt, (_nxt[0] - 1, _nxt[1])))
                                    else:
                                        to_move.append((_nxt, (_nxt[0] + 1, _nxt[1])))
                                    to_move = [(curr, _nxt)] + to_move
                                    continue
                                else:
                                    to_move.append(
                                        ((curr[0], curr[1] - 1), (_nxt[0], _nxt[1] - 1))
                                    )
                                    moved.add((curr, _nxt))

                    _map[curr[0]][curr[1]], _map[_nxt[0]][_nxt[1]] = (
                        _map[_nxt[0]][_nxt[1]],
                        _map[curr[0]][curr[1]],
                    )
                robot[0] += MOVESET[move]["r"]
                robot[1] += MOVESET[move]["c"]

    ans = 0
    for r, row in enumerate(_map):
        for c, char in enumerate(row):
            if char in {"O", "["}:
                ans += (r * 100) + c
    return ans


if __name__ == "__main__":
    print(f"Part 1 : {day15(MAP_1)}")
    print(f"Part 2 : {day15(MAP_2, part=2)}")
