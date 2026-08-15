class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx=1
        nums=list(set(nums))
        if len(nums)==0:
            return 0
        nums.sort()
        cnt=1
        for i in range(1,len(nums)):
            if abs(nums[i-1]-nums[i])==1:
                cnt+=1
                mx=max(mx,cnt)
            else:
                cnt=1
        return mx