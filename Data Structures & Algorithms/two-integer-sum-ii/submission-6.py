class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            c=target-numbers[i]
            if c in d:
                return [d[c]+1,i+1]
            d[numbers[i]]=i
        #two ptr approach
        l=0
        r=len(numbers)-1
        while l<r:
            curSum=numbers[l]+numbers[r]
            if curSum==target:
                return [l+1,r+1]
            elif curSum>target:
                r-=1
            else:
                l+=1
        return []
