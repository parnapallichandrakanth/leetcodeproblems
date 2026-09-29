class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        ans=[""]*len(heights)
        ordr=heights.copy()
        ordr.sort(reverse=True)
        for i in range(len(heights)):
            index=ordr.index(heights[i])
            ans[index]=names[i]
        return ans
