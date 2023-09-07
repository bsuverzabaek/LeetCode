class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valid = -1
        i = 0
        while i<len(flowerbed):
            if flowerbed[i]==0:
                left = 0
                if i-1>=0:
                    if flowerbed[i-1]==0:
                        left = 1
                else:
                    left = 1
                right = 0
                if i+1<len(flowerbed):
                    if flowerbed[i+1]==0:
                        right = 1
                else:
                    right = 1
                if right and left:
                    if valid==-1:
                        valid = 0
                    valid += 1
                    i += 1
            i += 1
        if n==0:
            return True
        if valid==-1:
            return False
        return valid>=n
