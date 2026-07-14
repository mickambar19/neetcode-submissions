class Solution:
    DELIMITER = "α"
    EMPTY = "ñ"
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return self.EMPTY
        return self.DELIMITER.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.EMPTY:
            return []
        return s.split(self.DELIMITER)
            