class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        template of binary search 
        ->  missing (additional conditions)
        return kth value from missing

        """
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            #missing=expected-actual
            missing=arr[mid]-(mid+1)
            if missing<k:
                left=mid+1
            else:
                right=mid-1
        return left+k

        