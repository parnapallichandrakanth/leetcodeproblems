class Solution:
    def isHappy(self, n: int) -> bool:
        st=set()
        if n==1:
            return True
        while n>1:
            n=sum([int(i)**2 for i in str(n)])
            if n in st:
                return False
                break
            st.add(n)
            if n==1:
                return True
            
        
             

