class Solution:
    def maxProfit(self, prices):
        res = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)

        return res


cls = Solution()
prices = [7,1,5,3,6,4]
print(cls.maxProfit(prices))
