#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def dfs(cur, ans):
            if cur is None:
                return
            dfs(cur.left, ans)
            ans.append(cur.val)
            dfs(cur.right, ans)

        dfs(root, ans)
        return ans


# @lc code=end
