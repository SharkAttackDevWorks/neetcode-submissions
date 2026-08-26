class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = defaultdict(int)

        for x in nums:
            frequency[x]+=1

        
        heap = []

        for x in frequency:

            heapq.heappush[heap, (frequency[x], x)]

            if len(heap)>2:
                heapq.heappop(heap)
            
        
        return [heap[0][1], heap[1][1]]
