class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res=[]
        map={"2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtrack(i,curstr):

        #base case
            if i==len(digits):
                res.append(curstr)
                return
            #recursive case
            for j in map[digits[i]]:
            
                backtrack(i+1,curstr+j)
        
        backtrack(0,"")
        return res
        
        