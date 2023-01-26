/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let p = 0;
    // Iterate through list
    for(i = 1 ; i < nums.length ; i++){
    // Check if number at original position is the same
        if(nums[p] != nums[i]){
            nums[p+1] = nums[i];
            p++;
        }
    }
    return p + 1;
};