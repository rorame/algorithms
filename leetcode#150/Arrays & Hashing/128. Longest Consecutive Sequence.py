class Solution:
    # neetcode solution
    def longestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

nums = [100,4,200,1,3,2]

cls = Solution()
print(cls.longestConsecutive(nums))


# nums = [9,1,4,7,3,-1,0,5,8,-1,6]
# nums_sorted = sorted(nums)
#
# res = 0
#
# for i in range(len(nums)-1):
#     if nums_sorted[i+1] - nums_sorted[i] == 1:
#         res += 1
#
# print(nums_sorted, res+1, sep="\n")