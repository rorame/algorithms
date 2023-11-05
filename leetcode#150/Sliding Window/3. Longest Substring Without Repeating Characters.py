class Solution:
    # мое решение - не ультимативное, на части тестов крашится из-за выхода поинтера за пределы последовательности
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        if len(set(s)) == len(s):
            return len(s)

        l, r = 0, 1
        res = s[l]
        curr = s[l]

        while r < len(s) - 1:
            if s[l] != s[r] and s[r] != s[r+1]:
                curr += s[r]
                res = max(res, curr)
            else:
                l = r
                curr = "" + s[l]

            r += 1

        return res, len(res)

    # neetcode's solution
    def neetcode_lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res