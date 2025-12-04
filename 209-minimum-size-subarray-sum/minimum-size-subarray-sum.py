class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        min_length=  (inf)
        curr_sum  initailze
        left is intialzed on 0th indexed
        looping over  length
        expansion of window until target
        desicion  if target achieved 
        save the no. of combination ( min )
        shrinking
        return min length of subarray
        
        """
        min_length=float('inf')
        curr_sum=0
        left=0
        n=len(nums)
        for right in range (n):
            curr_sum+=nums[right]
            while curr_sum>=target:
                min_length=min(min_length,right-left+1) # window size 
                curr_sum-=nums[left]
                left+=1
        return min_length if min_length < float('inf') else 0

        #   if  no. of min elements in subarray   +ive return else return 0
        




       
