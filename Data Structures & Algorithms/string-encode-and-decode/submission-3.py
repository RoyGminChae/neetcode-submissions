# delimiter design
# think assembly assignment in college

class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []
        for string in strs:
            lengths.append(len(string))
        
        pos = 0
        res = ""
        for i in range(len(strs)):
            string = strs[i]
            length = lengths[i]
            res += str(length) + "#" + string
        
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            
            length = int(length)

            res.append(s[i+1:i+1+length])
            i += length + 1

        return res



