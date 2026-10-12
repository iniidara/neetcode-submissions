class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char1 = list(s)
        char2 = list(t)
        return sorted(char1)==sorted(char2)