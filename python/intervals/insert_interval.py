from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        upperBound = len(intervals) -1
        lowerBound = 0
        while lowerBound < len(intervals):
            if newInterval[0] <= intervals[lowerBound][1]:
                break
            lowerBound += 1
        if lowerBound >= len(intervals):
            intervals.append(newInterval)
            return intervals
        while upperBound >= 0:
            if newInterval[1] >= intervals[upperBound][0]:
                break
            upperBound -= 1
        if upperBound < 0:
            intervals.insert(0,newInterval)
            return intervals
        
        left = []
        if lowerBound > 0:
            left = intervals[:lowerBound]

        if intervals[lowerBound][1] < newInterval[0]:
            left.append(lowerBound)
            left.append(newInterval)
        else:
            newInterval[0] = min(intervals[lowerBound][0],newInterval[0])
            left.append(newInterval)
        if upperBound > lowerBound and intervals[upperBound][0] > newInterval[1]:
            left.append(intervals[upperBound])
        else:
            left[-1][1] = max(intervals[upperBound][1],left[-1][1])
            
        right = []
        if upperBound < len(intervals):
            right = intervals[upperBound+1:]
        left += right
        return left

if __name__ == "__main__":
    sol = Solution()
    sol.insert([[1,5]],[2,3])