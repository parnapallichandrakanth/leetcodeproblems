class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum1=0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    sum1+=abs(i-j)
        return sum1