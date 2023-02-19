class Solution:
    def minOperations(self, n: int) -> int:
        # 39 => 100111
        #    => 101000
        #    => 100000
        #    => 0
        
        # 54 =>  110110
        #    =>  111000
        #    => 1000000
        #    => 0
        
        b = [int(x) for x in list("0" + bin(n)[2:])][::-1]
        
        res = 0
        while b:
            if b[0] == 0:
                b.pop(0)
            else:
                res += 1
                c = 0
                while b[0] == 1:
                    c += 1
                    b.pop(0)
                    if not b:
                        return res
                if c != 1:
                    b[0] = 1
        return res