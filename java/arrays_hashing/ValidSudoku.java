public class ValidSudoku {
    public boolean isValidSudoku(char[][] board) {
        //check cols
        int[] curNums = new int[9];
        for(int i=0;i<board[0].length;i++) {
            for(int j=0;j<board.length;j++) {
                curNums[j] = parseField(board[j][i]);
            }
            if(!isValid(curNums)) {
                return false;
            }
        }
        //check rows
        for(int i=0;i<board[0].length;i++) {
            for(int j=0;j<board.length;j++) {
                curNums[j] = parseField(board[i][j]);
            }
            if(!isValid(curNums)) {
                return false;
            }
        }
        //check grid boxes
        for(int i=0;i<board[0].length;i+=3) {
            for(int j=0;j<board.length;j+=3) {
                if(!isValid(parseSubBox(i,j,board,curNums))) {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean isValid(int[] nums) {
        int[] remainingNums = new int[9];
        for (int i=0;i<9;i++) {
            remainingNums[i] = 1;
        }
        for(int i=0;i<nums.length;i++) {
            if (nums[i] > -1) {
                if(remainingNums[nums[i]-1] > 0) {
                    remainingNums[nums[i]-1] = 0;
                } else {
                    return false;
                }
            }
        }
        return true;
    }

    public int parseField(char s) {
        if (s == '.') {
            return -1;
        }
        return s - '0';
    }

    public int[] parseSubBox(int i,int j, char[][] board, int[] curNums) {
        for(int k=0;k<3;k++) {
            for(int l=0;l<3;l++) {
                curNums[3*k+l] = parseField(board[i+k][j+l]);
            }
        }
        return curNums;
    }
}
