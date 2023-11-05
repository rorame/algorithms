def maxArea(height):
    # BRUTE FORCE neetcode O(n^2 )
    res = 0
    for l in range(len(height)):
        for r in range(l+1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
    return res

def maxArea_2(height):
    # neetcode solution with O(n)
    res = 0

    l, r = 0, len(height)-1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res


# мое решение перебирает не все пары чисел, поэтому оно не проходит
height = [2,3,10,5,7,8,9]

l, r = 0, len(height) - 1

# max_amount = 0
res = 0

while l < r:
    amount = (r - l) * min(height[l], height[r])
    res = max(res, amount)
    l += 1
    amount = (r - l) * min(height[l], height[r])
    res = max(res, amount)
    r -= 1

# print(res)