class Solution:
    def romanToInt(self, s: str) -> int:
# my solution
        s = [*s]

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0

        for i in reversed(range(len(s))):
            if roman[s[i]] <= roman[s[i - 1]] or i == 0:
                sum += roman[s[i]]
            else:
                sum += roman[s[i]] - roman[s[i - 1]]
                sum -= roman[s[i - 1]]
        return sum

# NeetCode solution
    def romanToInt_neetcode(self, s: str) -> int:
        s = [*s]

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
        res = 0

        for i in range(len(s)):
            if i + 1 <= len(s) and roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        return res




c = Solution()
print(c.romanToInt_neetcode('MCMXCVII'))