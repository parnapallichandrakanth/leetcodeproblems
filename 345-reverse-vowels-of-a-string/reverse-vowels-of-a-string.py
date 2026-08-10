def is_v(k):
    return k in "aeiouAEIOU"
      
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            while not is_v(s[left]) and left<right:
                left+=1
            while not is_v(s[right]) and left<right:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return ''.join(s)
        