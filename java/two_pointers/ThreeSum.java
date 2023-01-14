package two_pointers;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> sols = new ArrayList<>();
        Arrays.sort(nums);
        for(int left=0;left<nums.length-2;left++) {
            if(left>0 && nums[left-1] == nums[left]) continue;
            int mid = left+1;
            int right = nums.length-1;
            while(mid<right) {
                if(nums[left] + nums[mid] + nums[right] == 0) {
                    List<Integer> curSol = new ArrayList<>();
                    curSol.add(nums[left]);
                    curSol.add(nums[mid]);
                    curSol.add(nums[right]);
                    sols.add(curSol);
                    mid++;
                    while(mid<right && nums[mid-1]==nums[mid]) mid++;
                } else if(nums[left] + nums[mid] + nums[right] > 0) {
                    right--;
                } else {
                    mid++;
                }
            }
        }
        return sols;
    }
}
