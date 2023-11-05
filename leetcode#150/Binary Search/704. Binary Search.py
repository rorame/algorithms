def search(nums, target):
    low = 0
    hight = len(nums) - 1

    while low <= hight:
        mid = (hight + low) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            low = mid + 1
        else:
            hight = mid - 1
    return -1

nums = [-1,0,3,5,9,12]
target = 10

print(search(nums, target))