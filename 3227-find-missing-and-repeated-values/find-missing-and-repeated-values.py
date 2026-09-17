class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d={}
        for i in range(1,(len(grid)**2)+1):
            d[i]=0
        print(d)
        for i in grid:
            for j in i:
                d[j]=d.get(j,0)+1
        print(d)
        ans=[0]*2
        for key in d.keys():
            if d[key]==2:
                ans[0]=key
            if d[key]==0:
                ans[1]=key
        return ans
            
            

