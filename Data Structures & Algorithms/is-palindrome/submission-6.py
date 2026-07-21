class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [a for a in s if a.isalnum()]
        return s == s[::-1]