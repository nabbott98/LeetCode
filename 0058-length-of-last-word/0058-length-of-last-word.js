class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Use split method to separate words, the find length of the last one hence [-1]
        return len(s.split()[-1])