class Solution:
    # brute force O(n^2)
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    # hash table O(n)
    def twoSum_2(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in d:
                return [i, d[diff]]
            d[v] = i

nums = [3,2,4]
target = 6

c = Solution()
print(c.twoSum_2(nums, target))

