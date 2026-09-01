class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k=celsius+273.15
        F=(celsius*1.80)+32
        return [k,F]