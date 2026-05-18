class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "#" + s

        return code

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []

        while j < len(s):
            i = j
            while s[j] != '#':
                j += 1

            length = int(s[i : j])
            i = j + 1
            j = i + length
            word = s[i : j]
            res.append(word)

        return res
        
