class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        i str arr strs
        o list of lists where sublists contain anagrams of each other
        c order doesnt matter, strs only lcase eng letters
        e empty? return empty list
        t O(NlogN)
        s O(M*N)
        """ 
        '''
        loop over strs
        sort curr word
        use sorted word as key and actual word as value
        return values of map
        '''
        res = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)
        
        return list(res.values())