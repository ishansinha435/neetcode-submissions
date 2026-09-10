class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hmap;
        for (const auto& s : strs) {
            vector<int> key(26, 0);
            for (char c : s) {
                key[c - 'a']++;
            }
            string str_key = to_string(key[0]);
            for (int i = 1; i < 26; ++i) {
                str_key += "," + to_string(key[i]);
            }
            hmap[str_key].push_back(s);
        }
        vector<vector<string>> res;
        for (auto pairs : hmap) {
            res.push_back(pairs.second);
        }
        return res;
    }
};
