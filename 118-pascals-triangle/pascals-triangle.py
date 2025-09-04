class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        res=[[1]]
        two pointer
        temp  each row we will store
        pointer update
        res.append
        we will return
        
        """
        res=[[1]]
        for i in range(numRows-1):
            temp=[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])# adding values
            res.append(row)
        return res