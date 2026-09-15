class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words=s.split()
        ans=" ".join(words[:k])
        return ans
            