class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtraking(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue

                cur.append(candidates[i])
                backtraking(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        backtraking([], 0, target)

        return res