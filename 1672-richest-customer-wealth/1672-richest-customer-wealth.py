class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Calculate customer totals
        totals = [sum(all_accounts) for all_accounts in accounts]
        
        # Return the largest customer total
        return max(totals)
        
        