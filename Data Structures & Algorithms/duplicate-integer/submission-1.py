class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return len(nums)!=len(set(nums))
        d=set()
        for i in nums:
            if i in d:
                return True
            d.add(i)
        return False
        