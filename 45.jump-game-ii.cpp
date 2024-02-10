/*
 * @lc app=leetcode id=45 lang=cpp
 *
 * [45] Jump Game II
 */

// @lc code=start
class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) return 0;

        int steps = nums[0];
        int idx = 0;
        int jumps = 0;

        while ((steps + idx) < nums.size() - 1) {
            vector<int> tmp = vector<int>(nums.begin() + idx, nums.begin() + idx + steps + 1);
            for (int i = 0; i < steps + 1; i++){
                tmp[i] = i + tmp[i];
            }
            // find idx of max element
            int jump_idx = max_element(tmp.begin(), tmp.end()) - tmp.begin();
            idx += jump_idx;
            steps = nums[idx];
            jumps++;
        }

        return jumps + 1;
    }
};
// @lc code=end

