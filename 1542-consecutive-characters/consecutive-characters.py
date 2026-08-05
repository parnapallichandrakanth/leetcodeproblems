class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        max_count=0
        for i in range(len(s)-1):
            j=i+1
            if s[i]==s[j]:
                count+=1
            else:
                max_count=max(max_count,count)
                count=1
        return max(max_count,count)


                
        
        
        