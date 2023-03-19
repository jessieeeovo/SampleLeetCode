class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        # Weekly Contest 337, 03/19/2023
        res = [0, 0]
        b = bin(n)[2:]
        
        for i, n in enumerate(b[::-1]):
            if i % 2:
                res[1] += int(n)
            else:
                res[0] += int(n)
        return res