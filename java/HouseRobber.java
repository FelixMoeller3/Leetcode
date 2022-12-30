public class HouseRobber {
    public int rob(int[] nums) {
        int firstSum = 0;
        int secondSum = 0;
        for(int i=0;i<nums.length;i++) {
            int temp = Math.max(nums[i]+firstSum,secondSum);
            firstSum = secondSum;
            secondSum = temp;
        }
        return secondSum;
    }
}
