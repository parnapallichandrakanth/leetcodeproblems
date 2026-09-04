class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx=nums[0]
        mn=min(nums)
        for i in range(len(nums)):
            if nums[i]>mx:
                mx=nums[i]
            mn=min(nums[i:len(nums)])
            if mx-mn<=k:
                return i
        return -1

