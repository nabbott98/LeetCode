/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

const convertHelper = (nums: number[], start: number, end: number): TreeNode | null => {
    if(start > end) return null;
    
    let middle = Math.floor((start + end)/2);
    
    const root = new TreeNode(nums[middle]);
    
    root.left = convertHelper(nums, start, middle - 1);
    
    root.right = convertHelper(nums, middle + 1, end);
    
    return root;
};

const sortedArrayToBST = (nums: number[]): TreeNode | null => {
    let start = 0;
    let end = nums.length - 1;
    
    return convertHelper(nums, start, end);
};