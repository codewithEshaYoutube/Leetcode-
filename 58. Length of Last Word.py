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
# return len(s.strip().split()[-1])
