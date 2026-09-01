class Solution:
    def trap(self, height: List[int]) -> int:
        """
        i arr of non neg ints height
        o int total representing most amount of water between two bars
        c each i in height repersents its height with a width of 1
        e if height arr empty; early return 
        t O(N)
        s O(1)

        two ptrs based on container with most water
        init total 
        init ptrs on both ends 
        init max l and max r ints
        while l < r
            compare l and r
                if lmax smaller 
                    move l
                    potentially update max l
                    total += maxl - height[l] ? need check for negative
                if rmax smaller
                    move r
                    potentially update max r
                    total += maxr - height[r]
        
        return total
        """

        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        total = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(height[l], lmax)

                total += lmax - height[l]

            else:
                r -= 1
                rmax = max(height[r], rmax)
                
                total += rmax - height[r]
        
        return total