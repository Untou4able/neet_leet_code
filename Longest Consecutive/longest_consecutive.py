"""
 Mindbander.
 Very cleaver idea, i would've never come up with it.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq_len = 0
        nums_set = set(nums)
        for n in nums_set:
            if not n-1 in nums_set:
                seq_len = 1
                next_n = n + 1
                while next_n in nums_set:
                    seq_len += 1
                    next_n += 1
                if seq_len > max_seq_len:
                    max_seq_len = seq_len
        return max_seq_len

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
