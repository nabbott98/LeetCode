class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def even(n):
            count = 0
            while n != 0:
                n //= 10
                count += 1
            
            if count % 2 == 0:
                return 1
            else:
                return 0

        return sum(map(even, nums))