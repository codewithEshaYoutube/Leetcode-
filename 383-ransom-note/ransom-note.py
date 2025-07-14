class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_map={}
        
        for char in magazine :
            if char in char_map:
                char_map[char]+=1
            else:
                char_map[char]=1

        for char in ransomNote:
            if char not in char_map or char_map[char]==0:
                return False
            char_map[char] -= 1
        return True    
        

        
       


        