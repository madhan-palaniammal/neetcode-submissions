class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for num, f in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (f, num))
                continue

            topf, _ = heap[0]
            if topf < f:
                heapq.heappop(heap)
                heapq.heappush(heap, (f, num))
            
        res = []
        while heap:
            _, num = heapq.heappop(heap)
            res.append(num)

        return res
