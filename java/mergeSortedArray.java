import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums1Short = Arrays.copyOfRange(nums1,0,m);
        List<Integer> numList1 = new ArrayList<>(Arrays.stream(nums1Short).boxed().toList());
        List<Integer> numList2 = new ArrayList<>(Arrays.stream(nums2).boxed().toList());
        int curIndex = 0;
        while(!(numList1.isEmpty()) || !(numList2.isEmpty())) {
            if(numList1.isEmpty()) {
                nums1[curIndex] = numList2.remove(0);
            } else if(numList2.isEmpty()) {
                nums1[curIndex] = numList1.remove(0);
            } else {
                if (numList2.get(0) > numList1.get(0)) {
                    nums1[curIndex] = numList1.remove(0);
                } else {
                    nums1[curIndex] = numList2.remove(0);
                }
            }
            curIndex++;
        }
    }
}
