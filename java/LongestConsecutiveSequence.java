import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;

public class LongestConsecutiveSequence {
    public static int longestConsecutive(int[] nums) {
        HashSet<Integer> numSet = new HashSet<Integer>();
        Arrays.stream(nums).forEach(a -> numSet.add(a));
        int max = 0;
        for(int i=0;i<nums.length;i++) {
            if(numSet.contains(nums[i]-1)) continue;
            int seqLen = 1;
            while(numSet.contains(nums[i]+seqLen)) seqLen++;
            if (seqLen > max) max = seqLen;
        }
        return max;
    }
}
