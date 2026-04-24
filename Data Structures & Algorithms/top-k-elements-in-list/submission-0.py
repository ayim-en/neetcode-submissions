class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        i int arr nums and int k
        o k most frequent ints in nums
        c answers are always unique
        e empty list?
        t O(NLogK)
        s O(N+K)
        """

        count = {} # num, count

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for num in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res