class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        n=len(nums)
        while i < len(nums)-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            i+=2
            

        return nums[-1]


        
