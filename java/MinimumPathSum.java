import java.util.Arrays;

public class MinimumPathSum {
    public int minPathSum(int[][] grid) {
        if (grid.length == 1) {
            return Arrays.stream(grid[0]).sum();
        }
        if (grid[0].length == 1) {
            return Arrays.stream(grid).flatMapToInt(Arrays::stream).sum();
        }
        return grid[0][0] + Math.min(calcMinPathSum(grid, 1, 0), calcMinPathSum(grid, 0, 1));

    }

    public int calcMinPathSum(int[][] grid,int m, int n) {
        if (m == grid.length-1) {
            int sum = 0;
            for(int i=n;i<grid[m].length;i++) {
                sum+=grid[m][i];
            }
            return sum;
        }
        if (n == grid[0].length-1) {
            int sum = 0;
            for(int i=m;i<grid.length;i++) {
                sum+=grid[i][n];
            }
            return sum;
        }
        return grid[m][n] + Math.min(calcMinPathSum(grid, m+1, n), calcMinPathSum(grid, m, n+1));
    }
}
