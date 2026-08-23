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
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_len = 1

                while num + curr_len in num_set:
                    curr_len += 1
                
                max_len = max(curr_len, max_len)

        return max_len
                
