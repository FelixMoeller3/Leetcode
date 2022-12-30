import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class TopKFrequentElements {
    public int[] topKFrequent(int[] nums, int k) {
        int[] sol = new int[k];
        HashMap<Integer,Integer> freqCounts = new HashMap<>();
        for(int i=0;i<nums.length;i++) {
            freqCounts.put(nums[i],1+ freqCounts.getOrDefault(nums[i],0));
        }
        List<Integer> freqList = freqCounts.entrySet().stream().sorted((c,d) -> d.getValue().compareTo(c.getValue())).map(a -> a.getKey()).collect(Collectors.toList());
        for(int i=0;i<k;i++) {
            sol[i] = freqList.get(i);
        }
        return sol;
    }
}
