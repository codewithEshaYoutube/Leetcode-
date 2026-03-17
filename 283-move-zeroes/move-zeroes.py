class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        i=0
        j pointer iterate over len of array
        conditon j is sno zero (swap)
        i+=1
        """
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i] # swap 
                i+=1