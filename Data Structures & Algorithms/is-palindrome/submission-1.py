class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        i str s
        o bool true if s is a palindrome
        c s[i] can be any printable ASCII char, ignore case and non alpha num chars
        e s is a char long? if within ASCII constraint true
        t
        s

        init l & r ptrs on both ends of s
        compare vals at s[l] and s[r]
            if vals dont match; false
        
        need conditional for alphanum check and .lower for comparison
        """

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True