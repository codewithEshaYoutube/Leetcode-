class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        v,c=edges[0]
        a,b=edges[1]
        if v==a or v==b:
            return v
        return c
            
        
        