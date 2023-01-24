class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Iterate through list
        for i in range(len(nums)):
            # Find index of target or index of first number greater than target
            if nums[i] == target or nums[i] > target:
                return i
        # If target is greater than any number in list, return length of list
        return len(nums)
            