class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low =0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            guess=nums[mid]
            if guess<target:
                low=mid+1
            elif guess>target:
                high=mid-1
            else: 
                return mid
        return low    
