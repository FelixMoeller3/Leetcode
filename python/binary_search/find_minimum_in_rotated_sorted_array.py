from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            middle = (l+r)//2
            if nums[l] <= nums[middle]:
                if nums[middle]<=nums[r]:
                    return nums[l]
                l = middle+1
            else:
                r = middle
        return nums[l]

if __name__ == "__main__":
    sol = Solution()
    sol.findMin([3,4,5,1,2])
            