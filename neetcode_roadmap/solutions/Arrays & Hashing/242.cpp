//https://leetcode.com/problems/valid-anagram/

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        vector<int> vec(26);
        for(int i = 0; i < s.size(); i++) {
            vec[s[i] - 'a']++;
            vec[t[i] - 'a']--;
        }
        for (int n : vec) {
            if (n != 0) {
                return false;
            }
        }
        return true;
    }
};