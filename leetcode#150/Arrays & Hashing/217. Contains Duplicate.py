class Solution:
    # my solution
    def containsDuplicate(self, nums) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

    # neetcode's solution
    def containsDuplicate_neetcode(self, nums) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


nums = [1, 1]

c = Solution()
print(c.containsDuplicate(nums))
