class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hset;
        int res = 0;
        for (int n : nums) {
            hset.insert(n);
        }
        for (int n : hset) {
            if (!hset.contains(n - 1)) {
                int length = 1;
                while (hset.contains(n + length)) {
                    length++;
                }
                if (length > res) {
                    res = length;
                }
            }
        }
        return res;
    }
};
