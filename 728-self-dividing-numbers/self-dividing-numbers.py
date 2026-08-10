class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out=[]
        for i in range(left,right+1):
            lst=[int(j) for j in str(i)]
            count=0
            for y in lst:
                if y!=0:

                    if i%y==0:
                        count+=1
            if count==len(str(i)):
                out.append(i)
        return out



