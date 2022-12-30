import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;

class GroupAnagrams {
    public static List<List<String>> groupAnagrams(String[] strs) {
        List<HashMap<Character,Integer>> charCounts = new ArrayList<>();
        List<Integer> anagramIntegers = new ArrayList<>();
        for (String curStr: strs) {
            charCounts.add(computeCharCount(curStr));
        }
        List<List<String>> anagrams = new ArrayList<>();
        for(int i=0;i<strs.length;i++) {
            boolean found = false;
            for(int j=0;j<anagrams.size();j++) {
                HashMap<Character,Integer> a = charCounts.get(i);
                HashMap<Character,Integer> b = charCounts.get(anagramIntegers.get(j));
                if(isAnagram(a,b)) {
                    anagrams.get(j).add(strs[i]);
                    found = true;
                    break;
                }
            }
            if(!found) {
                anagramIntegers.add(i);
                List<String> newAna = new ArrayList<>();
                newAna.add(strs[i]);
                anagrams.add(newAna);
            }
        }
        return anagrams;
    }

    public static HashMap<Character,Integer> computeCharCount(String s){
        HashMap<Character,Integer> firstMap = new HashMap<>();
        for(int i=0;i<s.length();i++){
            char firstChar = s.charAt(i);
            firstMap.put(firstChar,1 + firstMap.getOrDefault(firstChar,0));
        }
        return firstMap;
    }


    public static boolean isAnagram(HashMap<Character,Integer> firstMap,
     HashMap<Character,Integer> secondMap){
        if (firstMap.size() != secondMap.size()) {
            return false;
        }
        for(Character c: firstMap.keySet()) {
            if(firstMap.get(c) != secondMap.getOrDefault(c,0)) {
                return false;
            }
        }
        return true;
    }
}