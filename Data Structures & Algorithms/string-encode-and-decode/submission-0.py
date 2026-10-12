class Solution:

    def encode(self, strs: List[str]) -> str:
        rStr = ""
        for st in strs:
            rStr += st + "#/"
        print(rStr)
        return rStr

    def decode(self, s: str) -> List[str]:
        prList = []
        wrdBgin = 0
        for i in range(len(s)):
            if s[i] == '/' and s[i-1] == '#':
                prList.append(s[wrdBgin:i - 1])
                wrdBgin = i + 1
        return prList
        
