class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #return sorted(s)==sorted(t)#simple but time o(nlogn)
       if len(s)!=len(t):
        return False
       f1={}
       f2={}
       for i in s:
        if i in f1:
            f1[i]+=1
        else:
            f1[i]=1
       for i in t:
        if i in f2:
            f2[i]+=1
        else:
            f2[i]=1
       return f1 == f2