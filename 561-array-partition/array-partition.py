class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res=0
        nums.sort()
        n=len(nums)
        i=0
        j=1

        while i<n and j<n:
            
            pair=(nums[j],nums[i])
            res+=min(pair)
            i+=2
            j+=2
        return res


