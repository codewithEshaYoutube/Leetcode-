class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        total sum
        left sum
        loop over array
        condition
        left_sum==right sum(total-left-current element)
        return index
        left+=nums[i]    0+1,
                         1+7

        """
        total_sum=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            if left_sum==total_sum-left_sum-nums[i]:
                return i
            left_sum=left_sum+nums[i]
        return -1
