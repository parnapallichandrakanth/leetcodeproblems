class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(0,32):
            if 4**i==n:
                return True
        return False