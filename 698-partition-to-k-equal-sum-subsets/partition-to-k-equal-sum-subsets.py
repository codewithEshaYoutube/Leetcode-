from typing import List
from functools import lru_cache

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        # Early pruning
        if nums[0] > target:
            return False

        n = len(nums)

        @lru_cache(None)
        def dfs(mask, curr_sum):
            """
            mask: bitmask representing which elements are used (1 = used)
            curr_sum: current subset sum so far
            """
            if mask == (1 << n) - 1:  # all numbers used
                return True
            
            # If we complete one subset, start a new one
            if curr_sum == target:
                return dfs(mask, 0)
            
            for i in range(n):
                if not (mask >> i) & 1 and curr_sum + nums[i] <= target:
                    if dfs(mask | (1 << i), curr_sum + nums[i]):
                        return True
            return False

        return dfs(0, 0)
