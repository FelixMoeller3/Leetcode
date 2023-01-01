public class TwoSum2_SortedInput {
    public int[] twoSum(int[] numbers, int target) {
        int[] sol = {0,numbers.length-1};
        while(numbers[sol[0]] + numbers[sol[1]] != target) {
            if(numbers[sol[0]] + numbers[sol[1]] < target) {
                sol[0]++;
            } else {
                sol[1]--;
            }
        }
        sol[0]++;
        sol[1]++;
        return sol;
    }
}
