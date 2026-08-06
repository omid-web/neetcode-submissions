class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # costruct hashmap of num and counts
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        # store the most frequent num in min heap, should only be k big 
        heap = []
        for num, count in count.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # return the num from (count, num) in desceding order from minheap
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res