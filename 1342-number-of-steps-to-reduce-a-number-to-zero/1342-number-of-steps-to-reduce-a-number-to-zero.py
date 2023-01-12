class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        
        while num > 0:
            #Increment step counter for every loop
            steps += 1
            
            # Check if num/2 = true if not subtract 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
        # Return the number of steps needed to reduce        
        return steps
            
        