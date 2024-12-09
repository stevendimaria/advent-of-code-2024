from collections import deque
from heapq import heappop, heappush
from tqdm import tqdm

EQS = []
with open("input.txt") as file:
    for line in file:
        eq = line.split()
        EQS.append([int(eq[0][:-1]), [int(x) for x in eq[1:]]])


def part1():
    ans = 0
    for eq in tqdm(EQS):
        pq = [[eq[0] - sum(eq[1]), eq[0], eq[1]]]
        while pq:
            rem, tot, nums = heappop(pq)
            if nums[0] > tot:
                continue
            if sum(nums) == tot:
                ans += tot
                break

            if len(nums) > 1:
                if (
                    sum(add_nxt := [nums[0] + nums[1]] + nums[2:]) == tot
                    or sum(mul_nxt := [nums[0] * nums[1]] + nums[2:]) == tot
                ):
                    ans += tot
                    break
                heappush(pq, [tot - sum(add_nxt), tot, add_nxt])
                heappush(pq, [tot - sum(mul_nxt), tot, mul_nxt])

    return ans


if __name__ == "__main__":
    print(f"Part 1 : {part1()}")
