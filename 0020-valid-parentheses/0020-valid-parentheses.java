class Solution {
    public boolean isValid(String s) {
        
        HashMap<Character, Character> map = new HashMap<>();
        map.put('}','{');
        map.put(']','[');
        map.put(')','(');
        
        Stack<Character> stack = new Stack<>();
        
        for (int i=0; i<s.length();i++) {
            if (map.containsValue(s.charAt(i))) {
                stack.push(s.charAt(i));
            } else {
                if (!stack.isEmpty()) {
                    char a = stack.pop();
                    if (a != map.get(s.charAt(i))) {
                        return false;
                }   
                } else {
                    return false;
                }
                    
            }
        }
                if (stack.isEmpty()) {
                    return true;
                } else {
                    return false;
                }
        
    }
}