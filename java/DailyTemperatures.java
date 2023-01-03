import java.util.Stack;

public class DailyTemperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] sol = new int[temperatures.length];
        Stack<Integer> prevTemps = new Stack<>();
        for(int i=0;i<temperatures.length;i++) {
            while(!(prevTemps.empty()) && temperatures[prevTemps.peek()] < temperatures[i]) {
                int curIndex = prevTemps.pop();
                sol[curIndex] = i-curIndex; 
            }
            prevTemps.push(i);
        }
        while(!prevTemps.empty()) {
            sol[prevTemps.pop()] = 0;
        }
        return sol;
    }
}
