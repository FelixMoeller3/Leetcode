import java.util.List;
import java.util.ArrayList;

class PascaslsTriangleTwo {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();
        res.add(1);
        for(int i=0;i<rowIndex;i++) {
            List<Integer> cur = new ArrayList<>();
            cur.add(1);
            for(int j=0;j<res.size()-1;j++) {
                cur.add(res.get(j)+res.get(j+1));
            }
            cur.add(1);
            res = cur;
        }
        return res;
    }
}