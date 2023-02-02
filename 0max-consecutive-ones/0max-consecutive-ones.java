class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        // Declare max 1s and hold variable
        int max1s = 0;
        int hold = 0;
        
        // Iterate through nums array
        for (int i = 0; i < nums.length; i++){
            if(nums[i] == 1) {
                hold++;
        	    max1s = Math.max(hold, max1s);    
            } else {
                hold = 0;
            }
        }
        // Check again last time since array may not end on 0
        return max1s;
    }
}