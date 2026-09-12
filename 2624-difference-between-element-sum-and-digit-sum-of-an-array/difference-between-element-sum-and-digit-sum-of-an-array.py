class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=sum(nums)
        digit_sum=0
        for i in nums:
            a=[int(x) for x in str(i)]
            digit_sum+=sum(a)
        return abs(element_sum - digit_sum)
            
