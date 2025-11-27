class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        while loop l<=r
        left , right 
        binary search
        mid  
        comparision with target
        return -1

        """
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            #  considering left sorted part 
            if nums[l]<=nums[mid]:
                if nums[l]  <= target< nums[mid]:
                    r=mid-1
                else:
                    l=mid+1

            # right
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1


            



        




