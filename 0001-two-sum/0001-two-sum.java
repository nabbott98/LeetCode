class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Brute force Method
        
        // Declare new array
        int [] arr = new int[2];
        // Iterate through nums array
        for(int i = 0; i < (nums.length - 1); i++){
            // Iterate through all following numbers
            for(int j = i + 1; j < nums.length; j++){
                // Test if numbers add up to target
                if(nums[i] + nums[j] == target){
                    arr[0] = i;
                    arr[1] = j;
                }
            }
        }
        return arr;
    }
}