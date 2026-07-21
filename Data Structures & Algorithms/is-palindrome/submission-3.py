class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = [a.lower() for a in s if a.isalnum()]
        return text == text[::-1]
            

        
        