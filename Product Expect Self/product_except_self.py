"""
 The idea is to calculate prefix product and postfix product in two gos which is O(2n) -> O(n)
 Never heared of prefix sum(running totals), haven't quite wrapped my head arount it
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        # prefix product
        for i in range(len(nums) - 1):
            answer[i+1] = answer[i] * nums[i]

        # postfix product and answer
        post_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * post_prod
            post_prod *= nums[i]
        return answer

s = Solution()
print(s.productExceptSelf([1,2,3,4]))