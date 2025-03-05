class Solution:
    def reverseVowels(self, s: str) -> str:
        # Use a set for O(1) vowel lookup
        vowels = set("aeiouAEIOU")  
        
        # Convert string to a list to allow modification
        s = list(s)  
        
        # Two-pointer approach
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move left pointer if s[l] is not a vowel
            if s[l] not in vowels:
                l += 1
                continue
            # Move right pointer if s[r] is not a vowel
            if s[r] not in vowels:
                r -= 1
                continue
            # Swap vowels
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        # Convert list back to string
        return "".join(s)  

# Time Complexity: O(n) -> We traverse the string once with two pointers.
# Space Complexity: O(n) -> We store the string as a list, requiring O(n) extra space.
