from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices of elements in decreasing order of values
        res = []       # result list to store max of each window

        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # 2. Maintain decreasing order in deque
            # Remove from back while current num is greater
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Once we reach window size 'k', record the max
            if i >= k - 1:
                res.append(nums[dq[0]])   # dq[0] is index of max element in current window

        return res
