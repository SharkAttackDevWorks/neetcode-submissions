class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        adic = defaultdict(int)

        for x in nums:
            adic[x]+=1

        
        alist = [(adic[key], key) for key in adic]

        alist.sort()

        output = []

        while len(output)< k:
            val, key = alist.pop(-1)
            output.append(key)

        
        return output