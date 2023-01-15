from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [-stone for stone in stones]
        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            firstStone = heapq.heappop(self.stones)
            secondStone = heapq.heappop(self.stones)
            if firstStone != secondStone:
                heapq.heappush(self.stones,firstStone-secondStone)
        if self.stones:
            return -self.stones[0]
        return 0