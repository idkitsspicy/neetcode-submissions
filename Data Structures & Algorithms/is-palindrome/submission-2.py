class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=""
        #clean up original string
        for i in s:
            if i.isalnum():
                k+=i.lower()
        l,r=0,len(k)-1
        while l<r:
            if k[l]!=k[r]:
                return False
            l+=1
            r-=1
        return True