class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using hasmap 
        num_map={}
        for n in nums:
            if n in num_map:
                return True # found duplicate
            num_map[n]= 1
        return False
        #T:O(n) S:O(n)
                
            
        

        