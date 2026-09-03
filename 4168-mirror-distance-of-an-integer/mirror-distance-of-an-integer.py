class Solution:
    def mirrorDistance(self, n: int) -> int:
        m=str(n)
        reverse=m[::-1]
        return abs(n-int(reverse))