class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx=0
        ms=0
        for lst in accounts:
            s=sum(lst)
            ms=max(ms,s)
        return ms