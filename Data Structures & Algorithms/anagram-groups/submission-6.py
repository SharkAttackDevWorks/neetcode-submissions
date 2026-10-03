class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        alist = []
        adic = {}
        

        for x in strs:
            astr = list(x)
            astr.sort()
            acount = "".join(astr)
            if acount not in adic:
                i = len(alist)
                alist.append([x])
                adic[acount] = i
            else:
                i = adic[acount]
                alist[i].append(x)

        return alist



