class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        reversed_num = num[::-1]
        
        if num == reversed_num:
            return True
        
        return False