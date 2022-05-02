from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsS = nums[:]
        numsS.sort()
        for i, x in enumerate(nums):
            print(i, x)
            try:
                numsS.index(target - x)
                j = nums.index(target - x)
                if not i == j:
                    return (i, j)
            except ValueError:
                continue
        return (-1, -1)

s = Solution()
answer = s.twoSum([3,2,4], 6)
print(answer)
