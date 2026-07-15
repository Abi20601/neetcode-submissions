class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for i in strs:
            x1 = sorted(i)
            x = "".join(x1)   
            # print(x)
            if x not in d:
                d[x] = []
            d[x].append(i)

        r = []
        for i,v in d.items():
            r.append(v)
        
        return r 