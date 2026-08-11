class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx=max(candies)
        ans=[]
        for i in range(len(candies)):
            if extraCandies+candies[i]>=mx:
                ans.append(True)
            else:
                ans.append(False)
        return ans