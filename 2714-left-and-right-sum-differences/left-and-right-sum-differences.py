class Solution(object):
    def leftRightDifference(self, nums):
        leftSum=[0]
        rightSum=[0]
        lsum=0
        rsum=0
        ans=[]
        for i in range(len(nums)-1):
            lsum+=nums[i]
            leftSum.append(lsum)
        for i in range(len(nums)-1,0,-1):#don't add last element(first element in array)
            rsum+=nums[i]
            rightSum.append(rsum)
        rightSum.reverse()
        for i in range(len(leftSum)):
            ans.append(abs(leftSum[i]-rightSum[i]))
        return ans

