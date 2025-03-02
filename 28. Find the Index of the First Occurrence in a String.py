class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0  # Edge case: empty needle should return 0
        
        if needle not in haystack:
            return -1  # If needle is not found in haystack, return -1
        
        return haystack.find(needle)  # Return the first occurrence index
#Solution 2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Implements the Knuth-Morris-Pratt (KMP) string matching algorithm.
        
        KMP efficiently finds the first occurrence of 'needle' in 'haystack' 
        by preprocessing 'needle' to avoid unnecessary comparisons.
        
        Time Complexity: O(N + M)
        - N: Length of haystack
        - M: Length of needle
        - We preprocess the pattern in O(M) time and perform the search in O(N) time.

        Space Complexity: O(M)
        - We store the LPS (Longest Prefix Suffix) array of size M.
        """

        # Edge case: If needle is an empty string, return 0
        if not needle:
            return 0  

        # Step 1: Build the LPS (Longest Prefix Suffix) array
        def build_lps(pattern):
            """
            Constructs the LPS (Longest Prefix Suffix) array.
            LPS helps in skipping unnecessary comparisons when a mismatch occurs.

            Time Complexity: O(M)
            Space Complexity: O(M)
            """
            lps = [0] * len(pattern)  # LPS array
            j = 0  # Tracks the length of the longest prefix suffix

            for i in range(1, len(pattern)):
                # Adjust j to the last matched prefix position
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]  # Backtrack using LPS

                # If characters match, increase j and store its value in LPS
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
            
            return lps

        # Precompute the LPS array for the needle (pattern)
        lps = build_lps(needle)

        # Step 2: Perform KMP search in haystack
        i, j = 0, 0  # Pointers for haystack and needle

        while i < len(haystack):
            if haystack[i] == needle[j]:  # Matching characters
                i += 1
                j += 1
                if j == len(needle):  # Full match found
                    return i - j  # Return the starting index of the match
            
            elif j > 0:
                j = lps[j - 1]  # Skip redundant checks using LPS
            
            else:
                i += 1  # Move forward in haystack

        return -1  # No match found
