def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (r + l) // 2
        if nums[m] == target:
            return m

        if nums[m] >= nums[l]: # left sorted portion
            if target < nums[l]:
                l = m + 1
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        else: # right sorted portion
            if target < nums[m]:
                r = m - 1
            elif target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1




nums = [4,5,6,7,0,1,2]
target = 5

print(search(nums, target))
