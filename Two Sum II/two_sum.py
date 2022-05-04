"""
 Seems like bsearch is not worth it, even if tweaked to return last search position for not found values.
"""
from typing import List


def bsearch(nums: List[int], low: int, hi: int, target: int) -> int:
    if hi - low <= 0:
        return -1
    mid = (low + hi) // 2
    if target == nums[mid]:
        return mid
    if target > nums[mid]:
        return bsearch(nums, mid+1, hi, target)
    if target <  nums[mid]:
        return bsearch(nums, low, mid, target)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            tar = target - n
            j = bsearch(numbers, i+1, len(numbers), tar)
            if j > 0:
                return [i+1, j+1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while True: # as long as we are guaranted to have a solution
            two_sum = numbers[i] + numbers[j]
            if two_sum == target:
                return [i+1, j+1]
            if two_sum > target:
                j -= 1
            else:
                i += 1

s = Solution()
print (s.twoSum2([2,3,4], 6))