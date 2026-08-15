class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in t:
            if i in d:
                d[i]-=1
                if d[i]==0:
                    d.pop(i)
            else:
                return i