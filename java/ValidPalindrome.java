public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        String filtered = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        for(int i=0;i<filtered.length()/2;i++) {
            if(filtered.charAt(i) != filtered.charAt(filtered.length()-i-1)) return false;
        }
        return true;
    }
}
