class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix*suffix
        output=[1]*len(nums)
        p=1
        for i in range(len(nums)):
            output[i]=p
            p*=nums[i]
        s=1
        for i in reversed(range(len(nums))):
            output[i]*=s
            s=s*nums[i]

        return output