with open("input.txt", "r") as file:
    INPUT = file.read().split()

MAP, MOVES = [], []
for line in INPUT:
    if line[0] not in {'^','>','<','v'}:
        MAP.append([x for x in line])
    else:
        MOVES.extend([x for x in line])
MOVESET = {
    '^': {'r': -1, 'c': 0},
    'v': {'r': 1, 'c': 0},
    '>': {'r': 0, 'c': 1},
    '<': {'r': 0, 'c': -1}
}

def part1(_map):
    robot = None
    for i in range(len(_map)):
        for j in range(len(_map[0])):
            if _map[i][j]=='@':
                robot = [i,j]

    for move in MOVES:
        _nxt_r = robot[0]+MOVESET[move]['r']
        _nxt_c = robot[1]+MOVESET[move]['c']
        _nxt_char = _map[_nxt_r][_nxt_c]
        if _nxt_char == '#':
            pass
        elif _nxt_char == '.':
            _map[robot[0]][robot[1]], _map[_nxt_r][_nxt_c] = _map[_nxt_r][_nxt_c], _map[robot[0]][robot[1]]
            robot = [_nxt_r, _nxt_c]
        else:
            seen, to_move = set(), []
            _r, _c = robot
            while _map[_r][_c] not in {'.', '#'}:
                temp = (_r+MOVESET[move]['r'], _c+MOVESET[move]['c'])
                to_move.append(((_r,_c),temp))
                _r, _c = temp
                seen.add(_map[_r][_c])
            if '.' in seen:
                while to_move:
                    curr, _nxt = to_move.pop()
                    _map[curr[0]][curr[1]], _map[_nxt[0]][_nxt[1]] = _map[_nxt[0]][_nxt[1]], _map[curr[0]][curr[1]]
                robot[0] += MOVESET[move]['r']
                robot[1] += MOVESET[move]['c']

        # print(f"Robot: {robot}")
        # print(f"Move {move}")
        # print(f"Next Move: {_nxt_r, _nxt_c}\nNext Char: {_nxt_char}")
        # for row in _map:
        #     print(''.join(row))
        # print()

    ans = 0
    for r, row in enumerate(_map):
        for c, char in enumerate(row):
            if char=='O':
                ans += (r*100)+c
    return ans


if __name__ == "__main__":
    print(f"Part 1 : {part1(MAP)}")
    # print(f"Part 2 : {part2()}")


