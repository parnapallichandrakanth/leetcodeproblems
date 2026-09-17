class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        for i in range(len(nums)//2):
            mn=min(nums)
            mx=max(nums)
            a=(mn+mx)/2
            avg.append(a)
            nums.remove(mn)
            nums.remove(mx)
        return min(avg)