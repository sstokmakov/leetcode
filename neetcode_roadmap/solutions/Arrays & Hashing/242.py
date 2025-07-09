# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums = [0] * 26
        for i in s:
            nums[ord(i) - ord('a')] += 1
        for i in t:
            nums[ord(i) - ord('a')] -= 1

        for i in range(len(nums)):
            if nums[i] != 0:
                return False
        return True