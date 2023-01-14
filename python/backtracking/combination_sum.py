from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        allCombs = []
        if target == 0:
            allCombs.append([])
        if target < 0:
            return []
        for i in range(len(candidates)):
            possibleCombs = self.combinationSum(candidates[i:],target-candidates[i])
            if not possibleCombs:
                continue
            for j in range(len(possibleCombs)):
                possibleCombs[j].append(candidates[i])
            allCombs += possibleCombs
        return allCombs

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2],1))