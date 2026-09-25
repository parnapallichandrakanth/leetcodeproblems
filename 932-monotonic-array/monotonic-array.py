class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if nums[0]<=nums[len(nums)-1]:
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:#checking condition when fails return False
                    return False
            return True
        elif nums[0]>=nums[len(nums)-1]:
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:#checking condition when fails return False
                    return False
            return True
                    
