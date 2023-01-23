class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Store old length
        oldLen = len(arr) 
        i = 0
        
        while i < oldLen :
            # Insert 0 into list
            if arr[i] == 0 :
                arr.insert(i+1 , 0)
                i += 1
            i += 1
        # Snip arr to old length
        arr[:] = arr[:oldLen]