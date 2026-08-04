class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        i str s and str t
        o bool true if s and t are anagrams of each other, else false
        c s and t only lcase eng letters
        e s and t are different lens? early return false
        t O(N)
        s 0(1)
        """

        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)

        if s_map == t_map:
            return True
        else:
            return False
