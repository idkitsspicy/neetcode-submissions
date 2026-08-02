class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        curr=0
        length=0
        #start with the minimum value in list and check for consecutive element
        for i in numset:
            if i-1 not in numset:
                curr=i
                length=1
            while curr+1 in numset:
                curr+=1
                length+=1
            longest=max(longest,length)
        return longest
                


        