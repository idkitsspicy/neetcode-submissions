class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                k = -(nums[i] + nums[j])

                if k in seen:
                    triplet = tuple(sorted([nums[i], nums[j], k]))
                    res.add(triplet)

                seen.add(nums[j])

        return [list(x) for x in res]