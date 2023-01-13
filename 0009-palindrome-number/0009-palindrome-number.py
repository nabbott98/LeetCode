class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Turn number into string
        num = str(x)
        # Save a reversed version of the string
        reversed_num = num[::-1]
        
        # If reversed = original return True since that is a palindrome
        if num == reversed_num:
            return True
        
        return False