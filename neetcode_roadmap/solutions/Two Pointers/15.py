# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for l in range(len(nums)):
            if l > 0 and nums[l - 1] == nums[l]:
                continue
            m = l + 1
            r = len(nums) - 1
            while m < r:
                res = nums[l] + nums[m] + nums[r]
                if res == 0:
                    ans.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while m < r and nums[m - 1] == nums[m]:
                        m += 1
                elif res > 0:
                    r -= 1
                else:
                    m += 1
        return ans