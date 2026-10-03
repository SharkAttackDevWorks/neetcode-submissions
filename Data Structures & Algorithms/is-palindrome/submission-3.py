class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        allowed = set(list("abcdefghijklmnopqrstuvwxyz"))


        slist = list(s)
        astr = ""
        for x in slist:
            if x.lower() in allowed:
                astr+=x.lower()

        slist.reverse()

        arev = ""
        for x in slist:
            if x.lower() in allowed:
                arev+=x.lower()

        print(astr)
        print(arev)

        return astr == arev

