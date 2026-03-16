class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        pointer placement
        while loop until overlap
        conditions 4
        alpha numeric
        empty
        not equal
        equal
        return bool
        """
        
        i=0
        j=len(s)-1
        while i<j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue

            if len(s)==0 :
                return True

            elif s[i].lower()!=s[j].lower():
                
                return False
            else:
                i+=1
                j-=1
                
        return True


       #T O(n)
       #S O(1)