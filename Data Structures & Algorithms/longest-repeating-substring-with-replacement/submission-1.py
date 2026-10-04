class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0

        best = 1

        acount = Counter(s[left:1])



        def removalcount(acounter):
            alist = [(acounter[key], key) for key in acounter]

            if len(alist) == 1: return 0

            alist.sort()



            alist = alist[:-1]

            total = sum(x[0] for x in alist)

            # print(alist, s[left:right], total)

            return total


        for right in range(1,len(s)):
            acount[s[right]]+=1

            if len(acount) == 1 : 
                best = max(best, right-left+1)
                continue

            while len(acount) > 0 and removalcount(acount) >k:
                acount[s[left]]-=1
                left+=1

            best = max(best, right-left+1)

            

        return best



            


