class Solution:
    def minSumOfLengths(self, a: List[int], t: int) -> int:
        f = lambda a:[*accumulate(map(lambda p:d[p]-d.get(p-t,-inf),
            d:={0:-1}|dict(zip(accumulate(a),count()))),min)]
        return (-1,r:=min(map(add,f(a),f(a[::-1])[::-1])))[r<inf]