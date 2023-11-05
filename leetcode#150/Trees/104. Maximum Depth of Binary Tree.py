import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive DFS O(n)
    def maxDepth_1(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth_1(root.left), self.maxDepth_1(root.right))

    # iterative DFS
    def maxDepth_2(self, root):
        if not root:
            return 0

        res = 1
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res

    # BFS O(n)
    def maxDepth_3(self, root):
        if not root:
            return 0

        lvl = 0
        q = collections.deque([root])

        while q:

            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lvl += 1
        return lvl