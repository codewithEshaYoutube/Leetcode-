from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array
        
        for i in range(len(nums) - 2):  # Step 2: Iterate through the array
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue
            
            left, right = i + 1, len(nums) - 1  # Two-pointer initialization
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move left and right pointers to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # Increase sum
                else:
                    right -= 1  # Decrease sum
        
        return res
