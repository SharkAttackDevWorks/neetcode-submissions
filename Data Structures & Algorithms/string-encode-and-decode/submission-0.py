class Solution:

    def encode(self, strs: List[str]) -> str:
        
        s = ""

        for x in strs:
            alen = len(x)

            s+=str(alen)
            s+="#"
            s+=x

        return s


    def decode(self, s: str) -> List[str]:

        strs = []

        start = 0

        #. 5#words

        while start < len(s):
            alength = ""
            for j in range(start, len(s)):
                if s[j] != "#":
                    alength+=s[j]
                else:
                    break

            alength = int(alength) 

            aword = "".join(s[start+2:start+2+alength])

            strs.append(aword)

            start = start+2+alength

        

        return strs

