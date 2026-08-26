class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        afrequency = defaultdict(int)

        for x in nums:
            afrequency[x]+=1

        
        heap = []

        for x in afrequency:

            heapq.heappush(heap, (afrequency[x], x))

            if len(heap)>k:
                heapq.heappop(heap)
            
        result = []

        for i in range(k):

            result.append(heap[i][1])

        return result