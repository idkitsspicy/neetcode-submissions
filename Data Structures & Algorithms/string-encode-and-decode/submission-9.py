class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "#" + s
        return code

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the '#'
            j = i
            while s[j] != "#":
                j += 1

            # Length of the next string
            length = int(s[i:j])

            # Extract the string
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # Move to the next encoded string
            i = j + 1 + length

        return res