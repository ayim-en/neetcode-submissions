class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        i arr of str strs
        o list of lists with anagrams paired together
        c strs is only lowercase english letters
        e empty list? return list with empty str
        t O(NlogN)
        s O(M*N)
        """
        res = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)
        
        return list(res.values())



