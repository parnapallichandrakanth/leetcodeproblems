class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]
        sum1=0
        for i in nums:
            sum1+=i
            prefix.append(sum1)
        leftSum,rightSum=0,0
        for i in range(len(nums)):
            leftSum=prefix[i]
            rightSum=prefix[len(nums)]-prefix[i+1]
            if leftSum==rightSum:
                return i
        return -1
        
