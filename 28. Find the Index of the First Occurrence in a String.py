class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0  # Edge case: empty needle should return 0
        
        if needle not in haystack:
            return -1  # If needle is not found in haystack, return -1
        
        return haystack.find(needle)  # Return the first occurrence index
