class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        i int arr numbers sorted in non-dec and int target
        o indicies that add up to target where i1 < i2 and i1 != i2
        c unique solution and O(1) space; 1-INDEXED!
        e numbers of len 2? must be numbers[1], numbers[2]
        t O(N)
        s O(1)

        two ptrs sol

        init l and r on each side of arr
        compare l + r to target
            if greater, move r ptr
            if less, move l ptr
            if equal, return indicies
        
        might need to add 1 to return
        """

        l, r = 0, len(numbers) - 1

        while l < r:
            num_sum = numbers[l] + numbers[r]

            if num_sum > target:
                r -= 1
                
            elif num_sum < target:
                l += 1
                
            else:
                return [l + 1, r + 1]
        