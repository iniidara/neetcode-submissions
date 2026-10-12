class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick boundary check: if lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Allocate a fixed list of 26 zeros (one for each letter 'a'-'z')
        # This takes fixed, negligible O(1) space
        char_counts = [0] * 26
        
        # Track frequencies using ASCII values relative to 'a'
        for i in range(len(s)):
            char_counts[ord(s[i]) - 97] += 1
            char_counts[ord(t[i]) - 97] -= 1
            
        # If all counts returned to 0, it's a perfect match
        for count in char_counts:
            if count != 0:
                return False
                
        return True
