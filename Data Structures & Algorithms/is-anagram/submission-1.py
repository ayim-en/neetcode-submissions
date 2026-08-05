class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        i str s and t
        o bool true if anagram of each other else false
        c s and t are only lcase eng letters
        e diff lens s and t? early return false
        t O(N)
        s O(1)
        """

        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}

        for c in range(len(s)):
            s_map[s[c]] = 1 + s_map.get(s[c], 0)
            t_map[t[c]] = 1 + t_map.get(t[c], 0)

        return s_map == t_map