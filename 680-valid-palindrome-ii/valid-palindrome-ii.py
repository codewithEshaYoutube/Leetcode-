class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Helper function to check if a substring is a standard palindrome
                def is_palindrome(l: int, r: int) -> bool:
                    return s[l:r+1] == s[l:r+1][::-1]
                
                # Check both choices: drop left OR drop right
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            
            left += 1
            right -= 1
            
        return True