class Solution:
    def isValid(self, char):
        asciiCode = ord(char)
        CAPITAL_LETTERS = 65
        LOWER_LETTERS = 97
        NUMBER = 48
        print(asciiCode)
        return CAPITAL_LETTERS <= asciiCode < CAPITAL_LETTERS + 27 or LOWER_LETTERS <= asciiCode < LOWER_LETTERS + 27 or NUMBER <= asciiCode < NUMBER + 9 


    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1
        s = s.lower()
        while i <= j:
            iIsValid = self.isValid(s[i])
            jIsValid = self.isValid(s[j])
            if not iIsValid:
                i+=1
                continue
            if not jIsValid:
                j-=1
                continue
            if iIsValid and jIsValid:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
        return True
            

        
        