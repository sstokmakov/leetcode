# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)

        ans = 0
        for n in unique:
            if n - 1 not in unique:
                curr = 1
                while n + 1 in unique:
                    curr += 1
                    n += 1
                ans = max(ans, curr)
        return ans