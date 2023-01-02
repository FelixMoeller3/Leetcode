import java.util.Stack;

public class EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        Stack<Integer> numStack = new Stack<>();
        for(String s:tokens) {
            if (isOperator(s)) {
                int second = numStack.pop();
                int first = numStack.pop();
                numStack.push(evaluate(first,second,s));
            } else {
                numStack.push(Integer.parseInt(s));
            }
        }
        return numStack.peek();
    }

    public boolean isOperator(String s) {
        return s.equals("+") || s.equals("*") || s.equals("-") || s.equals("/");
    }

    public int evaluate(int first, int second, String op){
        if(op.equals("*")) {
            return first * second;
        }
        if(op.equals("/")) {
            return first / second;
        }
        if(op.equals("-")) {
            return first - second;
        }
        return first + second;
    } 
}
