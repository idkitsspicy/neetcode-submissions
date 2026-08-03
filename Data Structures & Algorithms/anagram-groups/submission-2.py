class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        g={}
        l=[]
        for i in range(len(strs)):
            k="".join(sorted(strs[i]))
            d[i]=k
        #return keys with same values
        for key,val in d.items():
            if val not in g:
                g[val]=[]
            g[val].append(strs[key])
        return list(g.values())