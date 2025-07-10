# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        return list(hashmap.values())