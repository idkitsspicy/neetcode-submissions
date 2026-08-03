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
#------------------bucket sort-------#
'''class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums)+1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        ans = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans'''









        