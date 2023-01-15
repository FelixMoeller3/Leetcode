import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k,len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])
        return heap[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4],2))