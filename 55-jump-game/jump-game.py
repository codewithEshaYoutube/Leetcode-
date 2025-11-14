from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0  # farthest index we can reach

        for i in range(n):
            if i > max_reach:
                # Current index is not reachable
                return False
            # Update the farthest we can reach from here
            max_reach = max(max_reach, i + nums[i])

        return True  # if loop finishes, last index is reachable
