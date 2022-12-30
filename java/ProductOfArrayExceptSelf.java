public class ProductOfArrayExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int[] sol = new int[nums.length];
        int[] rightSide = new int[nums.length];
        rightSide[rightSide.length-1] = 1;
        for(int i=rightSide.length-2;i>-1;i--) {
            rightSide[i] = rightSide[i+1] * nums[i+1];
        }
        int leftSide = 1;
        for(int i=0;i<nums.length;i++) {
            sol[i] = leftSide*rightSide[i];
            leftSide*= nums[i];
        }
        return sol;
    }
}
