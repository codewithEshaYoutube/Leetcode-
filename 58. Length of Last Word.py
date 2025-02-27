class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        length=0
        while s[i] == " ":
             i-=1
        while i>=0 and s[i]!=" ":
            length=length+1
            i-=1
        

        
        return length
        # Time Complexity: O(N) - We may traverse the entire string in the worst case.
        # Space Complexity: O(1) - Only a few integer variables are used (constant space).


# Optimized solution using Python's built-in functions
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
    
        # Time Complexity: O(N)
        # - strip() removes leading/trailing spaces in O(N)
        # - split() splits the string into words in O(N)
        # - Accessing the last word and finding its length is O(1)
        
        # Space Complexity: O(N)
        # - split() creates a list of words, which takes extra space in the worst case.
