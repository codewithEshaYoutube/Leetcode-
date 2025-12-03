class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        # ---- MERGE SORT IMPLEMENTATION ----
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            result = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result
        
        # ---- SORT WITHOUT BUILT-IN SORT ----
        nums = merge_sort(nums)
        
        # ---- SLIDING WINDOW ----
        l, r = 0, k - 1
        res = float('inf')
        
        while r < len(nums):
            res = min(res, nums[r] - nums[l])
            l, r = l + 1, r + 1
        
        return res
