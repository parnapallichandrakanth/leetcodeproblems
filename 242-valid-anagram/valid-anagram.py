class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        f={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        return d==f   
        