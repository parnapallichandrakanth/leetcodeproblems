class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        lst=[int(i) for i in str(n)]
        d={}
        for i in lst:
            d[i]=d.get(i,0)+1
        sum1=0
        for i in d.keys():
            sum1+=i*d[i]
        return sum1
            