from collections import deque
from tqdm import tqdm


with open("input.txt") as file:
    RULES = {"": set()}
    UPDATES = []
    STARTS = set()
    for line in file:
        line = line[:-1]
        if "|" in line:
            k, v = line.split("|")
            RULES[""] |= {k}
            if not RULES.get(k):
                RULES[k] = set()
            RULES[k] |= {v}
            STARTS |= {k}
        elif "," in line:
            UPDATES.append(line.split(","))
        else:
            continue


def part1():
    ans, _incorrect = 0, []
    for _update in UPDATES:
        curr = _update[0]
        for n in _update[1:]:
            if n not in STARTS or n not in RULES[curr]:
                _incorrect.append(_update)
                break
            curr = n
        else:
            ans += int(_update[(len(_update) // 2)])

    return ans, _incorrect


def part2(incorrect: list):
    ans = 0

    for update in tqdm(incorrect):
        q = deque([("", [x for x in update], [])])
        while q:
            curr, rem, out = q.popleft()

            if not rem:
                if curr in RULES[out[-1]]:
                    out = out[1:] + [curr]
                    ans += int(out[len(out) // 2])
                break

            for i, n in enumerate(rem):
                if n not in STARTS and len(rem) > 1:
                    continue
                if n in RULES[curr]:
                    q.appendleft((n, rem[:i] + rem[i + 1 :], out + [curr]))
    return ans


if __name__ == "__main__":
    part1_ans, wrong = part1()

    print(f"Part 1 : {part1_ans}")
    print(f"Part 2 : {part2(wrong)}")
