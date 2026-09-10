class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < nums.size(); ++i) {
            int n = nums[i];
            if (n > 0) break;
            if (i != 0 and n == nums[i - 1]) continue;
            int l = i + 1, r = nums.size() - 1;
            while (l < r) {
                int currSum = n + nums[l] + nums[r];
                if (currSum < 0) {
                    l++;
                }
                else if (currSum > 0) {
                    r--;
                }
                else {
                    res.push_back({n, nums[l], nums[r]});
                    l++; r--;
                    while (l < r && nums[r] == nums[r + 1]) {
                        r--;
                    }
                }
            }
        }
        return res;
    }
};
