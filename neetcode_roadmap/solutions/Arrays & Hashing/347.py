# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            hashmap[n] += 1
        l = list(hashmap.keys())
        l.sort(reverse=True, key = lambda n: hashmap[n])
        return l[0:k]