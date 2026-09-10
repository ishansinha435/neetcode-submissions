class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hset(nums.begin(), nums.end());
        int res = 0;
        for (int n : hset) {
            if (!hset.contains(n - 1)) {
                int length = 1;
                while (hset.contains(n + length)) {
                    length++;
                }
                res = max(res, length);
            }
        }
        return res;
    }
};
