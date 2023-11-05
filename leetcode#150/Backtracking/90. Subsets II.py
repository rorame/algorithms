class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtraking(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtraking(i+1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1< len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtraking(i + 1, subset)

        backtraking(0, [])

        return res
