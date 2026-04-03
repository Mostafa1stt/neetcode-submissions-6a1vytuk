class Solution:
    N = 0
    def encode(self, strs: List[str]) -> str:
        global N
        N = len(strs)
        return "`".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s and N == 0:
            return []
        return s.split("`")
