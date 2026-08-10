class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst=list(s)
        right=len(s)-1
        left=0
        while left<right:
            if lst[left].isalpha():
                if lst[right].isalpha():
                    lst[left],lst[right]=lst[right],lst[left]
                    left+=1
                    right-=1
                else:
                    right-=1
            else:
                left+=1
        return "".join(lst)




            