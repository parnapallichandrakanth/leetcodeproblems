class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sub_cnt=0
        l=0
        r_cnt=0
        l_cnt=0
        for right in range(len(s)):
            if s[right]=='R':
                r_cnt+=1
            else:
                l_cnt+=1
            if r_cnt==l_cnt:
                sub_cnt+=1
                r_cnt=0
                l_cnt=0
        return sub_cnt
            