class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> buckets(nums.size() + 1);
        unordered_map<int, int> counts;
        for (int n : nums) {
            counts[n]++;
        }
        for (const auto& [num, count] : counts) {
            buckets[count].push_back(num);
        }
        vector<int> res;
        for (int i = buckets.size() - 1; i > -1; --i) {
            for (int n : buckets[i]) {
                res.push_back(n);
            }
            if (res.size() == k) {
                return res;
            }
        }
        return res;
    }
};
