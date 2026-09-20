class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for ch in s:
            if not st:
                st.append(ch)
            else:
                st.append(ch)
                if st[-1].isdigit():
                    if st[-2].isalpha():
                        st.pop()
                        st.pop()
        return "".join(st)