from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = (h-1 + min(piles)*len(piles))//h
        maxK = max(piles)
        hoursToEat = [0] * len(piles)
        while minK < maxK:
            middle = (minK + maxK) //2
            for i in range(len(hoursToEat)):
                hoursToEat[i] = (middle - 1+ piles[i]) // middle
            if sum(hoursToEat) <= h:
                maxK = middle
            else:
                minK = middle + 1

        return minK

if __name__ == "__main__":
    piles = [30,11,23,4,20]
    h = 6
    sol = Solution()
    sol.minEatingSpeed(piles,h)