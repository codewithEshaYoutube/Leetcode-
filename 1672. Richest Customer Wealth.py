class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum,accounts))
        

    # Time complexity O(m*n)    
    
    #  Space complexity O(m)
