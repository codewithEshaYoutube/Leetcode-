class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            guess=nums[mid]
            if guess==target:
                return mid
            elif guess<target:
                low=mid+1
            else:
                high=mid-1
            
        return low
            
        
        
         
        