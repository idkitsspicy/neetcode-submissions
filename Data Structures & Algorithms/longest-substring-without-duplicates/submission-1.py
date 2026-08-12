class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        seen=set()
        n=len(s)
        maxlen=0
        while r<n:
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                maxlen=max(maxlen,r-l)
            else:
                seen.remove(s[l])
                l+=1
        return maxlen
