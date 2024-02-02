#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#

# @lc code=start
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for idx, word in enumerate(words):
            if x in word:
                res.append(idx)
        return res
# @lc code=end

