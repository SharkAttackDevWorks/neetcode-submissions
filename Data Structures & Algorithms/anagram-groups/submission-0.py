class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        aset = deafaultdict(list)

        for x in strs:
            defaultdict[sorted(list(x))].add(x)
        


        return list(aset)