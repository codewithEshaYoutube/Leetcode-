class Solution:
    def singleNumber(self, nums: List[int]) -> int:


        result=0
        for num in nums:
            # exclusive or
            result = num ^ result
        return result
        
