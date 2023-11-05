class Solution:
    # my solution
    def countSubstrings(self, s: str) -> int:
        res = []

        for i in range(len(s)):

            # odd lenght
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r + 1])
                l -= 1
                r += 1

            # even lenght
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.append(s[l:r + 1])
                l -= 1
                r += 1

        return len(res)


    # neetcode's solution
    def countSubstrings_2(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.helper(s, i, i)
            res += self.helper(s, i, i + 1)
        return res

    def helper(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

