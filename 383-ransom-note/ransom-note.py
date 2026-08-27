class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d={}
        for i in magazine:
                d[i]=d.get(i,0)+1
        for i in ransomNote:
            if i in d.keys():
                if d[i]>0:
                    d[i]-=1
                else:
                    return False  
            else:
                return False
        return True


        
        