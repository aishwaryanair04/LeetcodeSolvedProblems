class Solution {
    public boolean isPalindrome(int x) {
        
        String x_string = Integer.toString(x);
        int l = 0;
        int r = x_string.length()  - 1;
        
        while (l < r) {
            if (x_string.charAt(l) != x_string.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        
        return true;
            
            
        
    }
}