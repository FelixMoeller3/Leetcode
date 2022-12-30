class Solution1 {
    public int removeDuplicates(int[] nums) {
        
        int dups = 0;
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]==nums[i+1]){
                nums[i]=42069;
                dups++;
            }
        }
        for(int i=1;i<nums.length;i++){
            if(nums[i]==42069){
                continue;
            }
            int oldIndex = i;
            int indexToPlace=i;
            while(indexToPlace>0 && nums[indexToPlace-1]==42069){
                indexToPlace--;
            }
            if(oldIndex!=indexToPlace){
                nums[indexToPlace] = nums[oldIndex];
                nums[oldIndex] = 42069;
            }
        }
        return nums.length-dups;
    }
}