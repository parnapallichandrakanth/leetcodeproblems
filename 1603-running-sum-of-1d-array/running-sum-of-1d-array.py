class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=[]
        runningSum=0
        for i in nums:
            runningSum+=i
            prefix.append(runningSum)
            
        return prefix
            