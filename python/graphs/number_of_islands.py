from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "1":
                    continue
                numIslands += 1
                self.markNeighbors(grid,i,j)
        return numIslands
    
    def markNeighbors(self, grid: List[List[str]], i:int, j:int):
        grid[i][j] = "B"
        if i < len(grid)-1 and grid[i+1][j] == "1":
            grid[i+1][j] = "B"
            self.markNeighbors(grid,i+1,j)
        if i > 0 and grid[i-1][j] == "1":
            grid[i-1][j] = "B"
            self.markNeighbors(grid,i-1,j)
        if j < len(grid[0]) - 1 and grid[i][j+1] == "1":
            grid[i][j+1] = "B"
            self.markNeighbors(grid,i,j+1)
        if j > 0 and grid[i][j-1] == "1":
            grid[i][j-1] = "B"
            self.markNeighbors(grid,i,j-1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands([["0","1","0"],["1","0","1"],["0","1","0"]]))