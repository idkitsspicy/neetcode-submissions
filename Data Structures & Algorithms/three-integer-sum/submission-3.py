class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #k=-(i+j)
        ans=[]
        for i in range(len(nums)):
            seen=set()
            for j in range(i+1,len(nums)): 
                k=-(nums[i]+nums[j])
                if k in seen:
                    ans.append(tuple(sorted([nums[i],nums[j],k])))
                seen.add(nums[j])
        res=set(ans)
        res=[list(x) for x in res]
        return res
