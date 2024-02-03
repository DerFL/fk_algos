#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = cur_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            # print(max_sum)
            cur_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, cur_sum)

        return max_sum / k
    
# @lc code=end

