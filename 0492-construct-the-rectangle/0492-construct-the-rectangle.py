import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.isqrt(area))
        while area % w != 0:
            w -= 1
        return [area // w, w]