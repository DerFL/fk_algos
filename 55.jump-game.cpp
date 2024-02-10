/*
 * @lc app=leetcode id=55 lang=cpp
 *
 * [55] Jump Game
 */

// @lc code=start
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int steps = nums[0];
        int idx = 0;

        while (steps > 0) {
            steps--;
            idx++;
            if (idx >= nums.size()) {
                return true;
            }
            steps = max(steps, nums[idx]);
        }
        return idx >= nums.size() - 1;
    }
};
// @lc code=end

