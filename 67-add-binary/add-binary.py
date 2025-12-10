class Solution:
    def addBinary(self, a: str, b: str) -> str:
        convert_a=int(a,2)
        convert_b=int(b,2)
        adding=convert_a+convert_b
        return bin(adding)[2:]
