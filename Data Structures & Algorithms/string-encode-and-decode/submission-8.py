class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#"
            encodedStr += s
        # print(encodedStr)
        return encodedStr


    def decode(self, s: str) -> List[str]:
        decodedStr = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#' and j < len(s):
                j += 1
            
            intLength = int(s[i:j])

            startChar = j + 1
            endChar = startChar + intLength
            strFound = s[startChar:endChar]
            # print(strFound)
            decodedStr.append(strFound)

            i = endChar

        return decodedStr
