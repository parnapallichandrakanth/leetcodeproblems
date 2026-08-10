def is_v(k):
    return k in "aeiouAEIOU"
      
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            if is_v(s[i]) and is_v(s[j]):
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif is_v(s[i]):
                j-=1
            elif is_v(s[j]):
                i+=1
            else:
                i+=1
                j-=1
        return ''.join(s)
        