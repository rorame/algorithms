def twoSum(numbers):
    pass

numbers = [-1,0]

target = - 1

l, r = 0, len(numbers) - 1

while l < r:
    if numbers[l] + numbers[r] == target:
        print(True)
        print(l+1, r+1)

    if numbers[l] + numbers[r] > target:
        r -= 1
    else:
        l += 1
