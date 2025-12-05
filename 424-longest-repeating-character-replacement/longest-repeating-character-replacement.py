from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        variable sliding window
        left , right pointer   window 
        res, max_count
        loop
        expansion
        storing the max
        conditions met  (k no. of changings)  next char is not like prev
        shrink
        storing the longest
        return res



        """
        count=defaultdict(int)
        left=0
        max_count=0
        result=0
        n=len(s)
        for right in range(n):
            count[s[right]]+=1
            max_count=max(max_count, count[s[right]])
            # invalid 
            while (right-left+1)-max_count>k:
                count[s[left]]-=1
                left+=1
            result=max(result,right-left+1)
        return result



        