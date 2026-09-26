class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        else:
            for i in range(len(nums)):
                mx=max(nums)
                nums.remove(mx)
                if i==2:
                    return mx
                    break
                    