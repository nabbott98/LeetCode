class Solution(object):
    def isValid(self, s):
        ack = []
        # Define proper pairings
        lookfor = {')':'(', '}':'{', ']':'['}

        # Check if there is a proper pair
        for p in s:
            if p in lookfor.values():
                ack.append(p)
            # if incorrect pop from final array
            elif ack and lookfor[p] == ack[-1]:
                ack.pop()
            else:
                return False

        return ack == []
        