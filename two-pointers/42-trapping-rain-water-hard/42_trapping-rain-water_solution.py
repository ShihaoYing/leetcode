#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        left = 0
        right = n - 1
        max_l = height[left]
        max_r = height[right]
        ans = 0
        while left < right:
            if max_l < max_r:
                ans += max_l - height[left]
                left += 1
                max_l = max(max_l, height[left])
            else:
                ans += max_r - height[right]
                right -= 1
                max_r = max(max_r, height[right])

        return ans


# @lc code=end
