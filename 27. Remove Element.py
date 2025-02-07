 class Solution:
    def removeElement(self, nums, val):  # Add 'self' for instance method
        i = 0  # Pointer to track placement of non-val elements

        for x in nums:
            if x != val:  
                nums[i] = x  # Move non-val element to position i
                i += 1  # Move pointer forward

        return i  # Return new length (number of non-val elements)

