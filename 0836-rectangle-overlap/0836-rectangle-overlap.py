class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        return (rec1[2] > rec2[0] and rec1[3] > rec2[1] and rec1[0] < rec2[2] and rec1[1] < rec2[3])