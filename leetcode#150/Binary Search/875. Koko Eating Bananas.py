import math


def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (r + l) // 2
        time = 0
        for p in piles:
            time += math.ceil(p / k)

        if time <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1

    return res


piles = [30,11,23,4,20]
h = 6

print(minEatingSpeed(piles, h))