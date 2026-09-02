class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k=len(nums)
        nums=set(nums)
        lst=[]
        for i in range(1,k+1):
            if i not in nums:
                lst.append(i)
        return lst