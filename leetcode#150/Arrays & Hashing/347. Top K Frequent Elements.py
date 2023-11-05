from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        countNums = {}

        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0)

        res = []

        for j in sorted(countNums.items(), key=lambda x:x[1], reverse=True)[0:k]:
            res.append(j[0])

        return res

    def my_solution(self, nums, k):
        res = Counter(nums).most_common(k)
        return [i[0] for i in res]

# nums = [4,1,-1,2,-1,2,3]
# k = 2
#
#
# countNums = {}
#
# for i in range(len(nums)):
#     countNums[nums[i]] = 1 + countNums.get(nums[i], 0)
#
# # сортировка массива по его значениям в обратном порядкеы
# # print(sorted(countNums.items(), key=lambda x:x[1], reverse=True))
#
# res = []
# for j in sorted(countNums.items(), key=lambda x:x[1], reverse=True)[0:k]:
#     res.append(j[0])
#
# print(res)