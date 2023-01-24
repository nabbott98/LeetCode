class Solution {
    public int searchInsert(int[] nums, int target) {
        // Iterate through list
        for (int i = 0; i < nums.length; i++){
            // Find index of target or index of first number greater than target
            if (nums[i] == target || nums[i] > target){
                return i;
            }
        }
        // If target is greater than any number in list, return length of list
        return nums.length;
    }
}