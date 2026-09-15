class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> counts;
        int l = 0, res = 0, most = 0;
        for (int r = 0; r < s.length(); ++r) {
            counts[s[r]]++;
            most = max(most, counts[s[r]]);
            while (r - l + 1 - most > k) {
                counts[s[l]]--;
                l++;
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};
