# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            ans = max(ans, curr)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans

s = "1"
s.isnumeric()