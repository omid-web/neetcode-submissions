class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # construct a max heap, priotiy of largest distance
        min_heap = [(-math.sqrt(x**2 + y**2), [x, y]) for x, y in points]
        heapq.heapify(min_heap)

        # pop from heap until size is k
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        # return list of k closest points to origin
        res = [[x, y] for d, [x, y] in min_heap]
        return res