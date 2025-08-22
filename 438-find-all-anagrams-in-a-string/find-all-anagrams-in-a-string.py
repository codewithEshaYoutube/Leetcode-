class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Approach:
        1. Create frequency dictionaries for p and the first window of s with size len(p).
        2. Compare both dictionaries:
            - If equal, add index 0 to result.
        3. Slide the window one step at a time:
            - Add the new character from the right.
            - Remove the old character from the left.
            - Update the hashmap counts.
            - If a character’s count becomes zero, remove it from hashmap to keep dictionary sizes small.
            - If updated hashmap matches p’s hashmap, record the starting index.
        4. Return the list of starting indices.

        Complexity:
        - Time complexity: O(n), where n = len(s), because each character is processed once when entering and once when leaving the window.
        - Space complexity: O(1), since the maximum hashmap size is bounded by 26 letters (constant space).
 
        """
        #hashmap
        if len(s)<len(p):
            return[]
        pCount,sCount={},{}
        for i in range(len(p)):
            pCount[p[i]]=1+pCount.get(p[i],0)
            sCount[s[i]]=1+sCount.get(s[i],0)
        res=[0] if sCount==pCount else []
        l=0
        for r in range(len(p),len(s)):
            sCount[s[r]]=1+sCount.get(s[r],0)
            sCount[s[l]]-=1
            if sCount[s[l]]==0:
                sCount.pop(s[l])
            l+=1
            if sCount==pCount:
                res.append(l)
        return res
        