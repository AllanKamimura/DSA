class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;

        while ((end - start) > 0) {
            while (start < end && !(Character.isLetterOrDigit(s.charAt(start)))) {
                start++;
            }

            while (start < end && !(Character.isLetterOrDigit(s.charAt(end)))) {
                end--;
            }

            char startValue = Character.toUpperCase(s.charAt(start));
            char endValue = Character.toUpperCase(s.charAt(end));

            if (startValue == endValue) {
                start++;
                end--;
            } else {
                return false;
            }
        }
        return true;
    }
}