import collections


class Solution:
    # my solution is correct, but it takes a lot of time!
    # O(k * (n - k))
    def maxSlidingWindow(self, nums, k):
        res = []
        window = []

        for i in range(k):
            window.append(nums[i])

        windowMax = max(window)
        res.append(windowMax)

        l = 0

        for r in range(k, len(nums)):
            window.remove(nums[l])
            window.append(nums[r])

            windowMax = max(window)

            res.append(windowMax)

            l += 1

        return res

    # O(1) * O(n)
    # Monotonically Decreasing Que
    def neetcode_maxSlidingWindow(self, nums, k):
        output = []
        q = collections.deque()  # index

        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # remove left value from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output