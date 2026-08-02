class Solution:
    def topKFrequent(self, nums, k):
        f = {}
        res = []

        # frequency map
        for i in nums:
            f[i] = f.get(i, 0) + 1

        for _ in range(k):
            # find key with max frequency
            max_key = max(f, key=f.get)
            res.append(max_key)
            del f[max_key]

        return res