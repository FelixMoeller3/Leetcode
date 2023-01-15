from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort(reverse=True)
        

    def add(self, val: int) -> int:
        pos = 0
        while pos<len(self.nums) and self.nums[pos] > val:
            pos += 1
        self.nums.insert(pos,val)
        return self.nums[self.k-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)