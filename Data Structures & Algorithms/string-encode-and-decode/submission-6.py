class Solution:
    
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}|{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            str_length = ""
            while 1:
                if s[j] == '|':
                    break
                str_length += s[j]
                j+= 1     
            str_length_n = int(str_length)
            result.append(s[j+1: j+1+str_length_n])
            i = j+1+str_length_n
        return result
            
            

