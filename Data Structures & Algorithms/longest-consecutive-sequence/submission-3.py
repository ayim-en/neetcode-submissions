class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        i int arr nums
        o str len of longest consecutive sequence
        c O(n) time complexity; elements are not always consecutive in nums
        e a consequtive sequence is one where nums[i + 1] = i + 1 for every element
        t O(N)
        s O(N)
        """
        num_set = set(nums)
        max_ctr = 0

        for num in num_set:
            if num - 1 not in num_set:
                ctr = 1

                while num + ctr in num_set:
                    ctr += 1
                
                max_ctr = max(ctr, max_ctr)

        return max_ctr
                
