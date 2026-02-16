class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }

        String xString = String.valueOf(x);

        Integer i = 0;
        Integer j = xString.length() - 1;

        while (i < j){
            char iChar = xString.charAt(i);
            char jChar = xString.charAt(j);

            if (iChar != jChar){
                return false;
            } else {
                i++;
                j--;
            }
        }
        return true;
    }
}