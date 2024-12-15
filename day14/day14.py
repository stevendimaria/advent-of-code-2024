from math import prod
from tqdm import tqdm


with open("input.txt", "r") as file:
    INPUT = file.read().split("\n")

MAP = []
for r in range(103):
    MAP.append([])
    for c in range(101):
        MAP[-1].append(0)

ROBOTS = {}
for i, data in enumerate(INPUT):
    pos, vel = data.split()

    pos = pos.split(',')
    pos_x = int(pos[0][2:])
    pos_y = int(pos[1])
    MAP[pos_y][pos_x] += 1

    vel = vel.split(',')
    vel_x = int(vel[0][2:])
    vel_y = int(vel[1])

    ROBOTS[i+1] = {'pos':(pos_x, pos_y), 'vel':(vel_x, vel_y)}


def part1(robots, _map, seconds, part=1):
    def calc_safety_factor():
        quadrants = [0, 0, 0, 0]
        for k, v in robots.items():
            c, r = v['pos']

            if c < 50 and r < 51:
                quadrants[0] += 1
            elif c > 50 and r < 51:
                quadrants[1] += 1
            elif c < 50 and r > 51:
                quadrants[2] += 1
            elif c > 50 and r > 51:
                quadrants[3] += 1
            else:
                continue

        return prod(quadrants)

    for sec in tqdm(range(seconds)):
        for k, v in robots.items():
            pos, vel = v['pos'], v['vel']

            x, y = pos
            _map[y][x] -= 1
            x = (x+vel[0])%101
            y = (y+vel[1])%103

            robots[k]['pos'] = (x, y)
            _map[y][x] += 1

        #########
        if part == 2:
            sf = calc_safety_factor()
            if sf < 200000000:
                print(sf, sec)
                f = open('part2.txt', 'a')
                f.write(f"{sec}\n")
                for line in _map:
                    line = ['.' if n == 0 else '*' for n in line]
                    f.write(f"{''.join(line)}\n")
                f.write(f"\n")
                f.close()
        #########

    return calc_safety_factor()



def part2(robots, _map, seconds):
    return part1(robots, _map, seconds, part=2)


if __name__ == "__main__":
    print(f"Part 1 : {part1(ROBOTS, MAP, 100)}")
    print(f"Part 2 : {part2(ROBOTS, MAP, 10000)}")



