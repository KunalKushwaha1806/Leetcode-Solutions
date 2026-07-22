import re
from bisect import bisect_left, bisect_right
from itertools import pairwise
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        total_ones = s.count("1")

        # Find all zero blocks
        zero_blocks = [(m.start(), m.end() - 1) for m in re.finditer("0+", s)]

        if not zero_blocks:
            return [total_ones] * len(queries)

        starts, ends = zip(*zero_blocks)
        block_count = len(zero_blocks)

        # Gain between adjacent zero blocks
        gains = []
        for (l1, r1), (l2, r2) in pairwise(zero_blocks):
            gains.append((r1 - l1 + 1) + (r2 - l2 + 1))

        # Build Sparse Table
        sparse = [gains]
        length = 1

        while length * 2 <= len(gains):
            prev = sparse[-1]
            curr = []

            for i in range(len(prev) - length):
                curr.append(max(prev[i], prev[i + length]))

            sparse.append(curr)
            length *= 2

        def query_max(left, right):
            if left > right:
                return 0

            k = (right - left + 1).bit_length() - 1
            size = 1 << k

            return max(
                sparse[k][left],
                sparse[k][right - size + 1]
            )

        def clipped_gain(index, left, right):
            gain = gains[index]

            gain -= max(0, left - starts[index])
            gain -= max(0, ends[index + 1] - right)

            return gain

        def best_gain(left, right):
            if block_count < 2:
                return 0

            first = bisect_left(ends, left)
            last = bisect_right(starts, right) - 2

            if first > last:
                return 0

            answer = max(
                clipped_gain(first, left, right),
                clipped_gain(last, left, right)
            )

            if last - first >= 2:
                answer = max(answer, query_max(first + 1, last - 1))

            return answer

        answer = []

        for left, right in queries:
            answer.append(total_ones + best_gain(left, right))

        return answer