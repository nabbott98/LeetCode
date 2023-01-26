class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort in place using [:] and sorted method use set method to remove duplicates
        nums[:] = sorted(set(nums))
        # Return the length
        return len(nums)