class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       import math
       def k_test(k):
        hrs=0
        for p in piles:
            hrs+=math.ceil(p/k)
        return hrs<=h
       
       l=1
       r=max(piles)
       #brute force with O(N)*MAX(piles)
       '''for k in range(1,r+1):
            if k_test(k):
                return k'''
       #binary search optimized
       while l<r:
        k=(l+r)//2
        if k_test(k):
            r=k
        else:
            l=k+1
       return l
