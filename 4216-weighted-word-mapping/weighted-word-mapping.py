class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        concat_str = ""
        for word in words:
            sm = 0
            for ch in range(len(word)):
                sm += weights[ord(word[ch])-ord('a')]
            sm = sm % 26
            rev = 25 - sm
            concat_str += chr(ord("a") + rev)
        return concat_str
