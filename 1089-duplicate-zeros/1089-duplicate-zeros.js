/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    // Iterate through list
    for (var i = 0; i < arr.length; i++) {
        // Check if that index has a zero
        if (arr[i] === 0) {
            // Splice and Delete if there is a trailing zero
            arr.splice(i, 0, 0);
            arr.pop();
            i += 1
        }
    }
};