#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # k=1 [1, 15, 7, 9, 2, 5, 10]
        # k=2 [15, 15, 7, 9, 9, 10, 10]
        # k=3 [15, 15, 15, 9, 10, 10, 10]
        # k=4 [15, 15, 15, 15, 10, 10, 10]
        # k=5 [15, 15, 15, 15, 15, 10, 10]
        # k=6 [15, 15, 15, 15, 15, 15, 10]
        # k=7 [15, 15, 15, 15, 15, 15, 15]

        res = 0
        n = len(arr)

        # Hint: Think dynamic programming: dp[i] will be the answer for array A[0], ..., A[i-1].
        # Hint: For j = 1, 2, ..., k, dp[i] will be the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j.

        dp = [0] * (n+1)

        for i in range(1, n+1):
            curMax = 0
            for j in range(1, min(k, i)+1):
                curMax = max(curMax, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + curMax * j)

        return dp[n]
# @lc code=end

