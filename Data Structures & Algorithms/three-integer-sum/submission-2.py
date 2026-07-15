class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        re = set()  # Use a set to store unique triplets
        nums.sort()
        
        for i in range(n):
            l = i + 1
            r = n - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    # Convert the triplet to a tuple before adding it to the set
                    re.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        
        # Convert the set of tuples back to a list of lists before returning
        return [list(triplet) for triplet in re]
        # for i in range(n):
        #     for j in range(i):
        #         for k in range(j):
        #             if(nums[i]+nums[j]+nums[k] == 0 and sorted([nums[i],nums[j],nums[k]]) not in r):
        #                 r.append(sorted([nums[i],nums[j],nums[k]]))
        
        # return r