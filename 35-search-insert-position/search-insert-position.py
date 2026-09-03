class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower=bisect.bisect_left(nums,target)
        return lower