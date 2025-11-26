class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            guess=nums[mid]

            if guess==target:
                return mid

            elif guess<target:
                l=mid+1
            else:
                r=mid-1
        return -1
        