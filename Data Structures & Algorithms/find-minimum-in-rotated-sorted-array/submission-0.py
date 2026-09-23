class Solution:
    def findMin(self, nums: List[int]) -> int:
        #return min(nums) ->O(n)
        #when rotated, produces sorted segemnts
        #eg 3456 and 12 and min ele will be first ele of right segment
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]



        
       

