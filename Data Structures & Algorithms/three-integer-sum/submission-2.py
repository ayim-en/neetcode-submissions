class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        i int arr nums
        o arr of triplets that sum to 0
        c i,j,k cannot equal each other; output and triplets in any order
            output arr can not contain dupe triplets
        e [0,1,2]; no gurantee of solution return empty arr
        t O(N^2)
        s O(1)* depends on sort algo

        init res
        sort nums
        loop over nums
        init k, l ptr k is +1 from j and l on other end
        check nums[i] + nums[j] + nums[k] == 0
            if greater move j
            if lesser move k
            if equal add values to res
        """

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            
            while j < k:
                if a + nums[j] + nums[k] > 0:
                    k -= 1

                elif a + nums[j] + nums[k] < 0:
                    j += 1

                else:
                    res.append([a,  nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        
        return res
