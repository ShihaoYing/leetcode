#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(cur, ans):
            if cur is None:
                return
            ans.append(cur.val)
            dfs(cur.left, ans)
            dfs(cur.right, ans)

        dfs(root, ans)
        return ans


# @lc code=end
