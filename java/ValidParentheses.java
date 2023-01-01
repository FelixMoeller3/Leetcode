import java.util.Stack;
import java.util.HashMap;

public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> charStack = new Stack<>();
        HashMap<Character,Character> closeToOpenMap = new HashMap<>();
        closeToOpenMap.put(')','(');
        closeToOpenMap.put(']','[');
        closeToOpenMap.put('}','{');
        for(int i=0;i<s.length();i++) {
            if(closeToOpenMap.containsValue(s.charAt(i))) {
                charStack.push(s.charAt(i));
            } else {
                if(charStack.empty() || charStack.peek().charValue() != closeToOpenMap.get(s.charAt(i)).charValue()) {
                    return false;
                }
                charStack.pop();
            }
        }
        return charStack.empty();
    }
}
