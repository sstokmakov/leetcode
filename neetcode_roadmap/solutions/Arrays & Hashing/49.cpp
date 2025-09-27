// https://leetcode.com/problems/group-anagrams/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;

        for (string& s : strs) {
            string sorted = s;
            sort(sorted.begin(), sorted.end());
            if (map.count(sorted) <= 0)
                map[sorted] = vector<string>();
            map[sorted].push_back(s);
        }
        vector<vector<string>> result;
        for (auto& entry : map) {
            result.push_back(move(entry.second));
        }
        return result;
    }
};