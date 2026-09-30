class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsSum=sum([int(i) for i in str(n)])
        squareSum=sum([int(i)*int(i) for i in str(n)])
        return squareSum - digitsSum >=50 