class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hmap;
        for (int i = 0; i < nums.size(); ++i) {
            int diff = target - nums[i];
            if (hmap.contains(diff)) {
                std::vector<int> res;
                res.push_back(hmap[diff]);
                res.push_back(i);
                return res;
            }
            hmap[nums[i]] = i;
        }
    }
};
