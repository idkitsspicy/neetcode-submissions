class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        seen = {}

        target = {}
        for c in s1:
            target[c] = target.get(c, 0) + 1

        while r < len(s2):
            if s2[r] not in target:
                seen = {}
                l = r + 1
            else:
                seen[s2[r]] = seen.get(s2[r], 0) + 1

                if r - l + 1 == len(s1):
                    if seen == target:
                        return True

                    seen[s2[l]] -= 1
                    if seen[s2[l]] == 0:
                        del seen[s2[l]]
                    l += 1

            r += 1

        return False