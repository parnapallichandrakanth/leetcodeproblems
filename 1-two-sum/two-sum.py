class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for slow in range(len(nums)):
            for fast in range(slow+1,len(nums)):
                if nums[slow]+nums[fast]==target:
                    return [slow,fast]
                else:
                    pass