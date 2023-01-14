from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        prevSubsets = self.subsets(nums[1:])
        newSubsets = []
        for subset in prevSubsets:
            curSubset = [nums[0]]
            for elem in subset:
                curSubset.append(elem)
            newSubsets.append(curSubset)
        return newSubsets + prevSubsets

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.subsets(nums))

