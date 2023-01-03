from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        timeToDest = []
        for i in range(len(position)):
            timeToDest.append((target-position[i])/speed[i])
        positionsAndTimes = list(zip(position,timeToDest))
        positionsAndTimes = sorted(positionsAndTimes,key=lambda x: x[0],reverse=True)
        orderedTimes = [time for _,time in positionsAndTimes]
        fleets.append(orderedTimes[0])
        for i in range(1,len(orderedTimes)):
            if(orderedTimes[i] > fleets[-1]):
                fleets.append(orderedTimes[i])
        return len(fleets)

if __name__ == "__main__":
    sol = Solution()
    sol.carFleet(12,[10,8,0,5,3],[2,4,1,1,3])