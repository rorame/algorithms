from collections import Counter


class Solution:
    def isAnagram_0(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

    def isAnagram_1(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False

    # neetcode's solution, but it's actually Time Limit Exceeded
    def isAnagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[[*s][i]] = 1 + countS.get([*s][i], 0)
            countT[[*t][i]] = 1 + countT.get([*t][i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


s = "aacc"
t = "ccac"

# print(sorted(s), sorted(t), sorted(s) == sorted(t), sep="\n")


# print(Counter(s))
# print(Counter(t))
# print(Counter(s) == Counter(t))

# TODO переписать конструкции [[*s][i]]