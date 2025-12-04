class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        res = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                res = min(res, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if res == float("inf") else res
