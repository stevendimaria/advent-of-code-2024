from math import prod


with open("input.txt", "r") as file:
    INPUT = file.read().split("\n")[:-1]

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


def part1(robots):
    for sec in range(100):
        for k, v in robots.items():
            pos, vel = v['pos'], v['vel']

            x, y = pos
            x += vel[0]
            y += vel[1]

            x = x%101 if 0<=x else x+101
            y = y%103 if 0<=y else y+103

            robots[k]['pos'] = (x, y)

    quadrants = [0,0,0,0]
    for k,v in robots.items():
        c, r = v['pos']

        if c<50 and r<51:
            quadrants[0] += 1
        elif c>50 and r<51:
            quadrants[1] += 1
        elif c<50 and r>51:
            quadrants[2] += 1
        elif c>50 and r>51:
            quadrants[3] += 1
        else:
            continue

    return prod(quadrants)

def part2():
    return 0


if __name__ == "__main__":
    print(f"Part 1 : {part1(ROBOTS)}")
    print(f"Part 2 : {part2()}")



