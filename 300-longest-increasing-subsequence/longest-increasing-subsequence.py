class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        LIS intializing
        looping
        setting pointer  i,j
        comparing i and j
        return max
        
        """

        LIS= [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])

        return max(LIS)
        
        #T :O(n^2)
        #S: O(n)