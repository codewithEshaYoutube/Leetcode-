class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        low and high pointer
        loop
        mid 
        comparisions
        return low or high
        """
        low =0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2 #  index
            guess=nums[mid]
            if guess==target:
                return mid
            elif guess>target:
                high=mid-1
            else:
                low=mid+1
        return low
        #T: O(logn)
        #S : O(1)
            

       