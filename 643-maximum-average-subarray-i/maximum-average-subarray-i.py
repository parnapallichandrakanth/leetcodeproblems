class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg=float('-inf')
        left=0
        currentSum=0
        for right in range(len(nums)):
            currentSum+=nums[right]
            if right>=k-1:
                avg=currentSum/k
                maxAvg=max(avg,maxAvg)
                #Subtracting the value on left (window Size is exceed k)
                currentSum-=nums[left]
                left+=1
        return maxAvg

                
                        
        