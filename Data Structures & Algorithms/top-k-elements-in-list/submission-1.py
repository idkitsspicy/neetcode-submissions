class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       #rank based on frequency
       f={}
       for i in nums:
        if i not in f:
            f[i]=1
        else:
            f[i]+=1
       #k greatest values and return corresponding keys
       ranks = sorted(f.items(), key=lambda x: x[1],reverse=True)
       ans=[num for num,freq in ranks[:k]]
       return ans









        