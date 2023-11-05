# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView(self, root):
        res = []
        q = collections.deque([root])

        while q:
            rightNode = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)

            if rightNode:
              res.append(rightNode.val)

        return res
