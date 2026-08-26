class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        aset = defaultdict(list)

        for x in strs:
            aset[sorted(list(x))].append(x)
        


        return list(aset)