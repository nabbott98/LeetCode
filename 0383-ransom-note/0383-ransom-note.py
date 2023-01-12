class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Define dictionary function to store ransom note letter counts
        def letter_count(s):
            d = {}
            for i in s:
                d[i] = d.get(i,0)+1
            return d
        
        ransom_dict = letter_count(ransomNote)
        
        # iterate through ransom dict and check if magazine letter count is greater than ransomnote, if not then return false
        for i in ransom_dict:
            if magazine.count(i) < ransom_dict[i]:
                return False
        return True
        