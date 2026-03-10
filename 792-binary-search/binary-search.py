class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2  #index
            guess=nums[mid]
            #descion

            if guess==target:
                return mid 
            elif guess >target:
                high=mid-1  #  update high
            else:
                low=mid+1 #update low
        return -1
        # T: O(logn)
        # S: O(1)   





        
        
        


        