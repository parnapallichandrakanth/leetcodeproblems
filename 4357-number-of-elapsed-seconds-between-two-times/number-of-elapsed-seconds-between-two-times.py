class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st=list(map(int,startTime.split(":")))
        end=list(map(int,endTime.split(":")))
        total=0
        i=0
        while i<=2:
            if i==0:
                if end[1]>=st[1]:
                    total+=(end[0]-st[0])*3600
                    i+=1
                else:
                    end[0]-=1
                    end[1]+=60
            if i==1:
                if end[2]>=st[2]:
                    total+=(end[1]-st[1])*60
                    i+=1
                else:
                    end[1]-=1
                    end[2]+=60
            if i==2:
                total+=end[2]-st[2]
                i+=1
        return total

            