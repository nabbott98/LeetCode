class Solution {
    public boolean isPalindrome(int x) {
        // Convert int into string
        String stringX = String.valueOf(x);
        
        // Find length of string
        int length = stringX.length() -1;
        
        // Iterate through string and check char at each end moving towards middle, if not equal return false
        for (int i = 0; i < length; i++){
            if (stringX.charAt(i) != stringX.charAt(length - i)){
                return false;
            }
        }
        return true;
    }
}