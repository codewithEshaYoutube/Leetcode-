from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)   # character frequency in window
        left = 0
        max_count = 0              # most frequent character count in window
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # if window is invalid → shrink from left
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # update longest valid window size
            result = max(result, right - left + 1)

        return result
