class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        res = 0
        for c in s:
            if c in seen:
                res += 1
                seen = set()
            seen.add(c)
        return res if not seen else res + 1