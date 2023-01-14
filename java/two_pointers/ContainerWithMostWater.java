package two_pointers;
public class ContainerWithMostWater {
    public static int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int max = -1;
        while(left < right) {
            int current = (right-left)*Math.min(height[left],height[right]);
            if(current > max) max = current;
            if(height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }
        return max;
    }
}
