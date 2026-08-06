class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count=0
        cnt=0
        substring=""
        
        for i in range(k):
            substring+=s[i]
            if s[i] in "aeiou":
                cnt+=1
        max_count=cnt
        for right in range(k,len(s)):
            substring+=s[right]
            if right>=k-1:
                if s[right] in "aeiou":
                    cnt+=1
                if substring[0] in "aeiou":
                    cnt-=1
                max_count=max(cnt,max_count)
                substring=substring[1:]
        return max_count
                




        