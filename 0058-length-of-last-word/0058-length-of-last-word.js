/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    // Use split method to separate words, the find length of the last one hence at(-1)
    // Use trim to remove whitespace at the end so that the split method returns an array with a word at the last index
    return s.trim().split(' ').at(-1).length
};