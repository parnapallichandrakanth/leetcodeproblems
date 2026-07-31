class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        l=list()
        x=list()
        for i in range(1,n+1):
            if i%m==0:
                l.append(i)
            else:
                x.append(i)
            
        sum1=sum(l)
        sum2=sum(x)
        return sum2-sum1