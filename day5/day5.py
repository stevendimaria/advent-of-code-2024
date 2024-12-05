class Node:

    def __init__(self, page: str):
        self.page = page
        self.children = []


with open("input.txt") as file:
    RULES = []
    UPDATES = []
    for line in file:
        line = line[:-1]
        if '|' in line:
            RULES.append(line.split('|'))
        elif ',' in line:
            UPDATES.append(line.split(','))
        else:
            continue


def part1():
    nodes = {'start': Node('start')}
    for first, second in RULES:
        if not nodes.get(first):
            nodes[first] = Node(first)
            nodes['start'].children.append(nodes[first])

        if not nodes.get(second):
            nodes[second] = Node(second)
            nodes['start'].children.append(nodes[second])

        nodes[first].children.append(nodes[second])

    ans = 0
    for _update in UPDATES:
        curr = nodes['start']
        for n in _update:
            if nodes.get(n) in curr.children:
                curr = nodes[n]
            else:
                break
        else:
            ans += int(_update[(len(_update)//2)])
    return ans


if __name__=='__main__':
    print(f"Part 1 : {part1()}")
    # print(f"Part 2 : {part2()}")