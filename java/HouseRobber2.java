import java.lang.Math;

public class HouseRobber2 {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return Math.max(nums[0],nums[1]);
        }
        int firstSum = 0;
        int secondSum = 0;
        int temp = 0;
        boolean isPartFirstSum = false;
        boolean isPartSecondSum = false;
        for(int i=0;i<nums.length-1;i++) {
            if (i==0) {
                isPartFirstSum = true;
            }
            temp = Math.max(firstSum+nums[i],secondSum);
            firstSum = secondSum;
            secondSum = temp;
        }
        if (isPartFirstSum) {
            secondSum = Math.max(firstSum-nums[0]+nums[nums.length-1],secondSum);
        } else {
            temp = Math.max(firstSum+nums[nums.length-1],secondSum);
            firstSum = secondSum;
            secondSum = temp;
        }
        return secondSum;
    }
}
