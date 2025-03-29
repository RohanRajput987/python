#Length of the Last Word

class Solution:
    def lengthOfLastWord(self, s: str):
        words = s.strip().split()
        return len(words[-1]) if words else 0

s = "Hello World"
sol = Solution()
print(sol.lengthOfLastWord(s))  # Output: 5
