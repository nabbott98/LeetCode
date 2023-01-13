class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def test(d):
            return max(d, key = d.get)
    
        def letter_count(s):
            d = {}
            for i in s:
                d[i] = d.get(i,0)+1
            return d
        
        return test(letter_count(nums))