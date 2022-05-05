""" i am dumb af """


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j and nums[i] < 1:
            while i > 0 and i < len(nums)-1 and nums[i] == nums[i-1]:
                i += 1
            k = i + 1
            j = len(nums) - 1
            while j > k:
                three_sum = nums[i] + nums[k] + nums[j]
                if three_sum > 0:
                    j -= 1
                elif three_sum < 0:
                    k += 1
                else:
                    res.add((nums[i], nums[k], nums[j]))
                    k += 1
                    while k < len(nums)-1 and nums[k-1] == nums[k]:
                        k += 1
            i += 1
        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
# [-4,-1,-1,0,1,2]
# [[-1,-1,2],[-1,0,1]]

#print(s.threeSum([-2,0,1,1,2]))
# [-2,0,1,1,2]
# [[-2,0,2],[-2,1,1]]

#print(s.threeSum([3,0,-2,-1,1,2]))
# [-2,-1,0,1,2,3]
# [[-2,-1,3],[-2,0,2],[-1,0,1]]
