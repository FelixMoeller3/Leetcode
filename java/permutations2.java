import java.util.List;
import java.security.Permissions;
import java.util.ArrayList;
import java.util.Arrays;

public class permutations2 {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        
        List<List<Integer>> permutations = getPermutations(nums);
        for (List<Integer> perm: permutations) {
            if(!isInList(perm,results)) {
                results.add(perm);
            }
        }
        return results;
    }

    public boolean isInList(List<Integer> item, List<List<Integer>> lists) {
        for(List<Integer> o: lists) {
            if (o!= null && o.equals(item)) {
                return true;
            }
        }
        return false;
    }

    public List<List<Integer>> getPermutations(int[]nums) {
        if (nums.length == 1) {
            List<List<Integer>> res = new ArrayList<>();
            List<Integer> f = new ArrayList<Integer>();
            f.add(nums[0]);
            res.add(f);
            return res;
        } else {
            Integer first = nums[0];
            List<List<Integer>> results = new ArrayList<>();
            List<List<Integer>> previousPerms = getPermutations(Arrays.copyOfRange(nums,1, nums.length));
            for (List<Integer> perm: previousPerms) {
                for(int i=0;i<=perm.size();i++){
                    List<Integer> temp = new ArrayList<>();
                    temp.addAll(perm);
                    temp.add(i,first);
                    results.add(temp);
                }
            }
            return results;
        }
    }

    public static void main(String[] args) {
        int[] nums = {1,1,3};
        permutations2 a = new permutations2();
        List<List<Integer>> perms = a.getPermutations(nums);
        for(List<Integer> test: perms) {
            String res = "[ ";
            for(Integer i: test) {
                res += i.toString() + " ";
            }
            res += "]";
            System.out.println(res);
        }
    }
}
