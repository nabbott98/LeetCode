/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Create new instance of the Map prototype
    let mp = new Map()
    // Iterate through nums array
    for (let i = 0; i < nums.length; i++) {
        let diff = target - nums[i]
        
        // look and see if mp has the difference
        if (mp.has(diff)) {
            return [i, mp.get(diff)]
        }
        
        mp.set(nums[i], i)
    }
};