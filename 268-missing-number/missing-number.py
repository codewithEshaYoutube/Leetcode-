class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        present=[False]*(n+1)
        for num in nums:
            present[num]=True
        for i in range(n+1):
            if  not present[i]:
                return i

        

            

        