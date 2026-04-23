class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            l = len(s)
            encoded_str += f"{l}:{s}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        
        i = 0
        while i < len(s):
            l = 0
            while s[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                d = int(s[i])
                l = (l * 10) + d
                i += 1

            i += 1
            if l > 0:
                decoded_str = s[i:i+l]
                strs.append(decoded_str)
                i += l
            else:
                strs.append("")

        return strs
            


