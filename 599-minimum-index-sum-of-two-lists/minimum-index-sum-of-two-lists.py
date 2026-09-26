class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        d={}
        ans=[]
        for i in range(len(list1)):
            if list1[i] in set(list2):
                d[list1[i]]=i+list2.index(list1[i])
        mn=min(d.values())
        for st in d.keys():
            if d[st]==mn:
                ans.append(st)
        return ans
