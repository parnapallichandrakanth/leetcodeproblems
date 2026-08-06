class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        first_window=arr[:k]
        CurrentSum=sum(first_window)
        count=0
        if CurrentSum/k>=threshold:
            count+=1
        for i in range(k,len(arr)):
            CurrentSum=CurrentSum+arr[i]-arr[i-k]
            if CurrentSum/k>=threshold:
                count+=1
        return count


