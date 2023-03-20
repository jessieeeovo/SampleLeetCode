class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if n == 0:
            return True
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            elif i + 1 < len(flowerbed) and flowerbed[i + 1] == 1:
                i += 3
            else:
                n -= 1
                if n == 0:
                    break
                i += 2
        return n == 0