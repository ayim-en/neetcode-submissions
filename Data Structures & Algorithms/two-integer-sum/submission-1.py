class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        i int arr nums and int target
        o indicies i and j that add up to target
        c i != j and unique solution
        e i and j same num? fine as long as diff indicies
        t O(N)
        s O(N)
        """

        pair = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in pair:
                return [pair[complement], i]
            
            pair[num] = i
