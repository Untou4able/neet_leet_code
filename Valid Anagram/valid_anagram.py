class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        for i, c in enumerate(t):
            try:
                s.remove(c)
            except ValueError:
                return False
        print(i)
        print(len(t))
        return len(s) == 0

s = Solution()
print(s.isAnagram("ab", "a"))
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
