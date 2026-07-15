class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        x = []
        for i,v in enumerate(nums):
            if target-v not in d:
                d[v] = i
            else:
                x.append(d[target-v])
                x.append(i)
                return x