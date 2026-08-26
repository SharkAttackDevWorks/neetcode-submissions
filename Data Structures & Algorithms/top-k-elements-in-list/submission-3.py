class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        afrequency = defaultdict(int)

        for x in nums:
            afrequency[x]+=1

        
        heap = []

        for x in afrequency:

            heapq.heappush(heap, (afrequency[x], x))

            if len(heap)>2:
                heapq.heappop(heap)
            
        
        return [heap[0][1], heap[1][1]]
