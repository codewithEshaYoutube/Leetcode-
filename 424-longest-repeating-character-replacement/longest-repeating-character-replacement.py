class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)  # Count of characters in current window
        left = 0
        max_count = 0  # Max frequency in current window
        result = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])
            
            # Check if current window is valid
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            # Update result
            result = max(result, right - left + 1)
        
        return result
