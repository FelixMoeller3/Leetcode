import java.util.List;

public class TestAlgos {
    public static void main(String[] args) {
        String[]grid = {"ac","c"};
        List<List<String>> result = GroupAnagrams.groupAnagrams(grid);
        System.out.println(result);
    }
}
