from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            countC = [0] * 26
            for c in word:
                countC[ord(c) - ord('a')] += 1
            group = d.setdefault(tuple(countC), list())
            group.append(word)
        return d.values()

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
