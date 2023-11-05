class Solution:
    def rob(self, nums):
        # [rob1, rob2, n, n+1, ...]
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

cls = Solution()
nums = [2,7,9,3,1]
print(cls.rob(nums))