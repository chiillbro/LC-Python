class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> track;
        for (int i = 0; i < nums.size(); ++i) {
            auto num = nums[i];
            auto it = track.find(target - num);

            if (it != track.end() && it->second != i) {
                return {it->second, i};
            }
            track[num] = i;
        }

        return {};
    }
};