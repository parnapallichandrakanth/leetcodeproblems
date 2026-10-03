class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d={}
        sum1=0
        for i in nums:
            d[i]=d.get(i,0)+1
        for key in d.keys():
            if d[key]==1:
                sum1+=key
        return sum1
