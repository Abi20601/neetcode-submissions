class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return True
        return False
        # n = len(nums)
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         if(nums[i] == nums[j]):
        #             return True
        # return False

        
        