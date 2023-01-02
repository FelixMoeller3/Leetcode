import java.util.LinkedList;

public class MinStack {
    private LinkedList<Integer> elements;
    private LinkedList<Integer> minList;
    public MinStack() {
        this.elements = new LinkedList<>();
        this.minList = new LinkedList<>();
    }
    
    public void push(int val) {
        this.elements.add(0,val);
        if (minList.size() == 0 || val <= this.minList.get(0).intValue()) {
            this.minList.add(0,val);
        }
    }
    
    public void pop() {
        int curElem = this.elements.remove().intValue();
        if(curElem == this.minList.get(0).intValue()) {
            this.minList.remove();
        }
    }
    
    public int top() {
        return this.elements.getFirst();
    }
    
    public int getMin() {
        return this.minList.get(0);
    }
}
