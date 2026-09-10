def canShip(weights,days_have,capacity):
    days_needed=0
    cWeightSum=0
    for weight in weights:
        if cWeightSum + weight <= capacity:
            cWeightSum += weight
        else:
            cWeightSum = weight
            days_needed+=1
    if cWeightSum!=0:
        days_needed+=1
    return days_needed<=days_have
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canShip(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low

