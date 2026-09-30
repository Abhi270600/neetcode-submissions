class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = collections.defaultdict(list)
        res = []

        for s in strs:
            
            key = "".join(sorted(s))

            hashmap[key].append(s)

        for k, v in hashmap.items():
            res.append(v)
        
        return res
