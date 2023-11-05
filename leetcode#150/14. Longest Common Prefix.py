class Solution:
    # neetcode's solution
    def longestCommonPrefix(self, strs) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or [*s][i] != [*strs[0]][i]:
                    return res
            res += [*strs[0]][i]
        return res

    # solution with zip function and set
    def longestCommonPrefix_2(self, strs) -> str:
        res = ""

        for i in zip(*strs):

            if len(set(i)) == 1:
                res += i[0]
            else:
                return res

        return res

strs = ["flower","flower","flower"]

c = Solution()
print(c.longestCommonPrefix_2(strs))

# TODO переписать конструкции [[*s][i]]

