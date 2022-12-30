import java.util.List;
import java.util.ArrayList;

class PascalsTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> first = new ArrayList<>();
        first.add(1);
        result.add(first);
        for(int i=1;i<numRows;i++) {
            List<Integer> cur = new ArrayList<>();
            cur.add(1);
            List<Integer> prev = result.get(i-1);
            for(int j=0;j<prev.size()-1;j++) {
                cur.add(prev.get(j)+prev.get(j+1));
            }
            cur.add(1);
            result.add(cur);
        }
        return result;
    }
}