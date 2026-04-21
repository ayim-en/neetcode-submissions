class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        i str s and str t
        o bool true if anagrams else false
        c only lc eng letters
        e empty? diff length? false
        t O(N)
        s O(1)
        """

        if len(s) != len(t):
            return False
        
        s_map, t_map = {}, {}

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        
        return s_map == t_map