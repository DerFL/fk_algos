#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

# reference: https://labuladong.online/algo/di-ling-zh-bfe1b/yi-ge-fang-894da/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        return self.nSumTarget(nums, 3, 0, 0)
    
    def nSumTarget(self, nums, n, start, target):
        N = len(nums)
        ans = []

        if n < 2 or N < n:
            return ans
        
        if n == 2:
            left, right = start, N - 1

            while left < right:
                left_val, right_val = nums[left], nums[right]
                total = left_val + right_val

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    ans.append([left_val, right_val])

                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1

        else:
            for i in range(start, N):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])

                for arr in sub:
                    ans.append([nums[i]] + arr)
        
        return ans

# @lc code=end

