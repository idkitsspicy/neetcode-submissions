class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d={}
        # g={}
        # l=[]
        # for i in range(len(strs)):
        #     k="".join(sorted(strs[i]))
        #     d[i]=k
        # #return keys with same values
        # for key,val in d.items():
        #     if val not in g:
        #         g[val]=[]
        #     g[val].append(strs[key])
        # return list(g.values())
        #------frequency of characters----#
        l=defaultdict(list)
        for s in strs:
            cou=[0]*26
            for i in s:
                cou[ord(i)-ord('a')]+=1
            l[tuple(cou)].append(s)
        return list(l.values())



