#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rst = len(nums)
        for i, val in enumerate(nums):
            rst += i - val
        return rst 
# @lc code=end

