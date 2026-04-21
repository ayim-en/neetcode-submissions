class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        i int arr nums and int target
        o indices i and j
        c nums[i] + nums[j] == target and i != j
        e duplicates? yes
        t O(N)
        s O(N)
        """

        checked = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in checked:
                return [checked[complement], i]
            
            checked[num] = i