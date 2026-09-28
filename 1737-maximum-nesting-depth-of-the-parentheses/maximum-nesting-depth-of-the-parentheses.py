class Solution:
    def maxDepth(self, s: str) -> int:
        mx=0
        st=[]
        for ch in s:
            if ch=="(":
                st.append(ch)
                mx=max(len(st),mx)
            if len(st)==0:
                continue
            if ch==")":
                st.pop()
        return mx

                    
                 