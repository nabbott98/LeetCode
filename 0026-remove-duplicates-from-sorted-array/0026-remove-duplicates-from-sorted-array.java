class Solution {
    public int removeDuplicates(int[] nums) {
        int p = 0;
        // Iterate through list
        for(int i = 1 ; i < nums.length ; i++){
        // Check if number at original position is the same
            if(nums[p] != nums[i]){
                nums[p+1] = nums[i];
                p++;
            }
        }
        return p + 1;
    }
}