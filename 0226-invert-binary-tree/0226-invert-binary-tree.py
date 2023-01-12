# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Check if root is empty at the top to avoid putting the below chunk inside a conditional
        if root == None:
            return root
        
        # Destructure in order to avoid defining a holding variable
        root.left, root.right = root.right, root.left
        
        # Use recursion on left tree
        self.invertTree(root.left)
        
        # Use recursion on right tree
        self.invertTree(root.right)
        
        return root