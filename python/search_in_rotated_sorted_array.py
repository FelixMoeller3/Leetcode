from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        shift = self.findMin(nums)
        l = shift
        r = (shift + length - 1)%length
        
        while l != r:
            middle = ((l-shift+(r-shift)%length)//2 + shift) % length if l>r else (l+r)//2
            if nums[middle] > target:
                r = (middle - 1)%length if middle!=l else middle
            elif nums[middle] < target:
                l = (middle+1)%length
            else:
                return middle

        if nums[l] == target:
            return l
        return -1


    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            middle = (l+r)//2
            if nums[l] <= nums[middle]:
                if nums[middle]<=nums[r]:
                    return l
                l = middle+1
            else:
                r = middle
        return l

if __name__ == "__main__":
    sol = Solution()
    sol.search([5,1,2,3,4],4)