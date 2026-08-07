class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        FirstWindow=s[0:len(p)]
        d1={}
        d2={}
        for i in FirstWindow:
            d1[i]=d1.get(i,0)+1
        for i in p:
            d2[i]=d2.get(i,0)+1
        ans=[]
        if d1==d2:
            ans.append(0)
        for right in range(len(p),len(s)):
            d1[s[right]]=d1.get(s[right],0)+1
            d1[s[right-len(p)]]-=1
            if d1[s[right - len(p)]] == 0:
                d1.pop(s[right-len(p)])
            if d1==d2:
                ans.append(right-len(p)+1)
        return ans





        