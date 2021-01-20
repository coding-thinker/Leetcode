#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start

import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # k-size min heap
        self.nums = nums[:]
        self.k = k
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:    
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif len(self.nums) == self.k and val > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)
        return self.nums[0]

    




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

