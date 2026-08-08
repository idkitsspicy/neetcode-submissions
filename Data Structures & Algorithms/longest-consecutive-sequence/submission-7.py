class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        store = set(nums)
        res = 0

        for num in store:
            # Only start counting if num is the beginning
            # of a consecutive sequence
            if num - 1 not in store:
                curr = num
                streak = 0

                while curr in store:
                    streak += 1
                    curr += 1

                res = max(res, streak)

        return res