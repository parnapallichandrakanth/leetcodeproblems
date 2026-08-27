class Solution(object):
    def topKFrequent(self, nums, k):
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        sorted_d=sorted(d.items(),key=lambda t:t[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sorted_d[i][0])
        return ans
