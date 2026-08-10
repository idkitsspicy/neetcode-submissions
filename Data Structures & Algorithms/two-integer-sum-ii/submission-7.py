class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since sorted, we can use a two-pointer approach to check if sum is less/greater than target
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]<target:
                
                l+=1
            elif numbers[l]+numbers[r]>target:
                
                r-=1
            else:
                return [l+1,r+1]
