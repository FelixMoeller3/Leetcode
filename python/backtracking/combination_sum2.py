from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        return self.combSum2(candidates,target)


    def combSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if target < 0 or not candidates:
            return []
        allCombs = []
        for i in range(len(candidates)):
            if i>0 and candidates[i] == candidates[i-1]:
                continue
            curCombs = self.combSum2(candidates[i+1:], target-candidates[i])
            if not curCombs:
                continue
            for j in range(len(curCombs)):
                curCombs[j].append(candidates[i])
                allCombs.append(curCombs[j])
        return allCombs


if __name__ == "__main__":
    sol = Solution()
    l = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(sol.combinationSum2(l,30))