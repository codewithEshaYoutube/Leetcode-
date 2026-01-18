class Solution:
    def largestOddNumber(self, num: str) -> str:
        res=[]
        for i in range(len(num)):
            if int(num[i])%2!=0:
                res.append(i)
        if not res:
            return ""

            
        return num[:max(res)+1]

        