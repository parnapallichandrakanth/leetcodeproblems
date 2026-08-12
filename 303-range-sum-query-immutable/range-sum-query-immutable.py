class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        current_sum=0
        prefix_sum=[]
        for i in range(len(self.nums)):
            current_sum+=self.nums[i]
            prefix_sum.append(current_sum)
        if left==0:
            return prefix_sum[right]
        else:
            return prefix_sum[right]-prefix_sum[left-1]
        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)