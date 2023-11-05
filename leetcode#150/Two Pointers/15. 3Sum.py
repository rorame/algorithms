def threeSum(nums):

    res = []
    nums.sort()

    for i, v in enumerate(nums):
        if i > 0 and nums[i-1] == v:
            continue

        l,  = i+1, len(nums) - 1

        while l < r:
            treeSum = v + nums[l] + nums[r]
            if treeSum > 0:
                r -= 1
            elif treeSum < 0:
                l += 1
            else:
                res.append([v, nums[l], nums[r]])
                l += 1
                while nums[l-1] == nums[l] and l < r:
                    l += 1
    return res