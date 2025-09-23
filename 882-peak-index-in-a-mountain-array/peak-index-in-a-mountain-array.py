from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            # If mid element is less than next → peak is on the right
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left   # or right (they meet at peak)
