from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for i in range(0,len(intervals)-1):
            if intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
            else:
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1],intervals[i+1][1])
        res.append(intervals[-1])
        return res

if __name__ == "__main__":
    sol = Solution()
    sol.merge([[1,3],[2,6],[8,10],[15,18]])