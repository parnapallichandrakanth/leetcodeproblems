class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix+Hashmap Solution
        cSum=0#this is our prefix sum
        subCount=0
        seen={0:1}
        for i in nums:
            cSum+=i
            req=cSum-k
            if req in seen:
                subCount+=seen[req]
            seen[cSum]=seen.get(cSum,0)+1
        return subCount