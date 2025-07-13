# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        curr = 1
        for i in range(len(nums)):
            res[i] = curr
            curr *= nums[i]
        curr = 1
        for i in reversed(range(len(nums))):
            res[i] *= curr
            curr *= nums[i]
        return res