from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        allPerms = []
        prevPerms = self.permute(nums[1:])
        for elem in prevPerms:
            for i in range(len(elem)+1):
                newElem = elem.copy()
                newElem.insert(i,nums[0])
                allPerms.append(newElem)
        return allPerms

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3]))