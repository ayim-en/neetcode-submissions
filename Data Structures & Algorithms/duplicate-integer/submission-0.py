class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        i int arr nums
        o bool true if duplicates else false
        c 
        e empty arr? return false
        t O(N)
        s O(N)
        """

        checked = set()

        for num in nums:
            if num in checked:
                return True

            checked.add(num)

        return False
