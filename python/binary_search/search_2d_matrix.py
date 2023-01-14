from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])
        left = 0
        right = len(matrix) * rowLen -1
        while left < right:
            middle = (left+right)//2
            if matrix[middle//rowLen][middle%rowLen] < target:
                left = middle+1
            elif matrix[middle//rowLen][middle%rowLen] > target:
                right = middle-1
            else:
                return True
        if matrix[left//rowLen][left%rowLen] == target:
            return True

        return False

if __name__ == "__main__":
    sol = Solution()
    sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)