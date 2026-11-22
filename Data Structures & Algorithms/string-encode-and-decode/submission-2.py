class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += ("§" + s)

        return result + "§"

    def decode(self, s: str) -> List[str]:
        result = []
        pre = -1
        for i in range(len(s)):
            if s[i] == "§":
                if pre >= 0 and i < len(s):
                    result.append(s[pre:i])
                pre = i+1
        
        
        return result