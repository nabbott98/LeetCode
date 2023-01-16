class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max = 0
        
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] == 1: 
                count += 1
            elif count > max:
                    max = count
                    count = 0
            else:
                count = 0
                
        if count > max:
            max = count
                
        return max