class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #the idea is to replace the one with less freq with the one with more
        l=0
        r=0
        max_f=0
        ans=0
        f={}
        #for current window, char with most freq
        for r in range(len(s)):
            f[s[r]]=f.get(s[r],0)+1
            max_f=max(max_f,f[s[r]])
            while (r-l+1)-max_f>k:
                f[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
            
        