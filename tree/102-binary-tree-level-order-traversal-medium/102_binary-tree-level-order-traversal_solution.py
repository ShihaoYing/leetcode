#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        ans = []
        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                leaf = queue.pop(0)
                if leaf is not None:
                    level.append(leaf.val)
                    queue.append(leaf.left)
                    queue.append(leaf.right)
            if level:
                ans.append(level)
        return ans


# @lc code=end
