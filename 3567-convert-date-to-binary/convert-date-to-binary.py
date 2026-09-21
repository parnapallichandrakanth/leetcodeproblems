class Solution:
    def convertDateToBinary(self, date: str) -> str:
        lst=list(map(int,date.split("-")))
        ans=[]
        for i in lst:
            ans.append(bin(i)[2:])
        return "-".join(ans)