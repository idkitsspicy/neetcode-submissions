class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":   # ✅ fix here
                j += 1

            leng = int(s[i:j])
            st = s[j+1:j+1+leng]

            res.append(st)
            i = j + 1 + leng

        return res