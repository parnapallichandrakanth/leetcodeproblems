class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        d={}
        max_length=0
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            if d[s[right]]>1:
                while d[s[right]]>1:
                    d[s[left]]-=1
                    left+=1
            max_length=max(max_length,right-left+1)
        return max_length         
