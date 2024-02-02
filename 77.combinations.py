#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# references: 
# ref1: https://labuladong.online/algo/di-ling-zh-bfe1b/hui-su-sua-c26da/
# ref2: https://labuladong.online/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-56e11/

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0:
            return self.res
        track = []

        self.backtrack(n, k, 1, track)
        
        return self.res

    def backtrack(self, n, k, start, track) -> None:
        # record the set when the length of the set is k
        if len(track) == k:
            self.res.append(track[:])
            return
        
        # increment from start to n
        for i in range(start, n+1):
            track.append(i)
            self.backtrack(n, k, i+1, track)

            # backtrack
            track.pop()

# @lc code=end
