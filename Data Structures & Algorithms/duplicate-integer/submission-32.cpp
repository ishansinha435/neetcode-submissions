class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hset;
        for (int n : nums) {
            if (hset.contains(n)) {
                return true;
            }
            hset.insert(n);
        }
        return false;
    }
};