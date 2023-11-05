def findMin(nums):
    l, r = 0, len(nums) - 1
    curr_min = float("inf")

    while l <= r:
        m = (r + l) // 2
        curr_min = min(curr_min, nums[m])

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1
    return curr_min

nums = [11,13,15,17]

print(findMin(nums))

