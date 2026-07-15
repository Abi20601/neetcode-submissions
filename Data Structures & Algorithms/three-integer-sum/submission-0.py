class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        r = []
        for i in range(n):
            for j in range(i):
                for k in range(j):
                    if(nums[i]+nums[j]+nums[k] == 0 and sorted([nums[i],nums[j],nums[k]]) not in r):
                        r.append(sorted([nums[i],nums[j],nums[k]]))
        
        return r