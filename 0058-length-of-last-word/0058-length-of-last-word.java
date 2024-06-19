class Solution {
    public int lengthOfLastWord(String s) {
        
        String[] listS = s.split(" ");
        
        List<String> temp = new ArrayList<>();
        
        for (int i=0; i< listS.length; i++) {
            if (!listS[i].equals(" ")) {
                temp.add(listS[i]);
                    }   
                }
        if (!temp.isEmpty()) {
            return temp.get(temp.size() - 1).length();
        } else {
            return 0; // If no valid words are found
        }
            }
        }