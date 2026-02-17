class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0;

        int lenS = s.length();
        int lenT = t.length();

        for (int j = 0; j < lenT;j++) {
            if (i >= lenS) {
                break;
            }

            char sValue = s.charAt(i);
            char tValue = t.charAt(j);

            if (sValue == tValue) {
                i++;
            }
        }
        if (i == lenS) {
            return true;
        } else {
            return false;
        }
    }
}