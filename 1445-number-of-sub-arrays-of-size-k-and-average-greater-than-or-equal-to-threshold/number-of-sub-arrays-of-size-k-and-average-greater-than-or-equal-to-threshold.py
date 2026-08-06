class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        Sub_sum=0
        cnt=0
        for right in range(len(arr)):
            Sub_sum+=arr[right]
            if right>=k-1:
                avg=Sub_sum/k
                if avg>=threshold:
                    cnt+=1
                Sub_sum-=arr[left]
                left+=1
        return cnt



