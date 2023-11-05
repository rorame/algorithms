class Solution:
    # my solution with O(n+m)
    # It's just a draft
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        l = 0

        # Implement set with all letters in s1, technically it's set contain all permutations
        charSet_res = set()
        for i in s1:
            charSet_res.add(i)

        charSet = set()
        # for r in range(len(s2)): # the width of our slide window depends on the length of s1
        #     while l < r:
        #         charSet.add(s2[r])
        #         r += 1
        #     if charSet == charSet_res:
        #         return True
        #
        # return False

        # O(n)
    def neetcode_checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
            else:
                0

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1

        return matches == 26