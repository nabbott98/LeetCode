class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for i in range(1, n + 1):
            # Test for i/3 & i/5 
            if i%3 == 0 and i%5 == 0:
                output.append("FizzBuzz")
                
            # Test i/3
            elif i%3 == 0:
                output.append("Fizz")
                
            # Test i/5
            elif i%5 == 0:
                output.append("Buzz")
                
            # If nothing hits, print string of i
            else:
                output.append(str(i))
                
        return output