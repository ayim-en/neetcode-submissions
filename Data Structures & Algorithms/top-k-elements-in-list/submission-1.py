class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        i int arr nums and int k
        o k most frequent elements in nums
        c answer is always unique, answer can be in any order
        e single element in nums? return the element
        t O(NLogK)
        s O(N+K)
        """
        '''
        two ideas: 
            iterate over nums with freq map and sort based on the values (desc order) 
            in the map loop over for first k elements
            
            freq map then place into min heap based on freq map value then pull first k elements
        '''
        import heapq

        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        heap = []

        for num in freq:
            heapq.heappush(heap, (-freq[num], num))

        res = []

        for i in range(k):
            val, num = heapq.heappop(heap)
            res.append(num)
        
        return res