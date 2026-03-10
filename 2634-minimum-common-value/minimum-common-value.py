class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def BinarySearch(arr,target):
            low=0
            high=len(arr)-1
            while low<=high:
                mid=(low+high)//2
                

                if arr[mid]==target:
                    return True

                elif arr[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
               
            return False
        for num in nums1:
            if BinarySearch(nums2,num):
                return num
        return -1



            
        