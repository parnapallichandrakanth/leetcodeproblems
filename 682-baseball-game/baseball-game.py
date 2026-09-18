class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for op in operations:
            if op.isalpha():
                if op =="D":
                    st.append(st[-1]*2)
                else:
                    st.pop()
                print(st)
            elif op=="+":
                print(op, st)
                st.append(st[-1]+st[-2])
            else:
                st.append(int(op))
                print(st)

        return sum(st)
        