class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        totals = [sum(all_accounts) for all_accounts in accounts]
        return max(totals)
        
        