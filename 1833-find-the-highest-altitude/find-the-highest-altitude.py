class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes=list(itertools.accumulate(gain,initial=0))
        return max(altitudes)
        