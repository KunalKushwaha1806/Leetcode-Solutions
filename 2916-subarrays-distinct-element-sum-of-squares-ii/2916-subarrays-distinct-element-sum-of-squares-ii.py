class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.MOD = 1_000_000_007
        self.tree_sum = [0] * (4 * n)
        self.tree_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _apply(self, node: int, l: int, r: int, val: int):
        length = r - l + 1
        # (c + val)^2 = c^2 + 2*val*c + val^2
        self.tree_sq[node] = (self.tree_sq[node] + 2 * val * self.tree_sum[node] + val * val * length) % self.MOD
        self.tree_sum[node] = (self.tree_sum[node] + val * length) % self.MOD
        self.lazy[node] += val

    def _push(self, node: int, l: int, r: int):
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            self._apply(2 * node, l, mid, self.lazy[node])
            self._apply(2 * node + 1, mid + 1, r, self.lazy[node])
            self.lazy[node] = 0

    def update(self, node: int, l: int, r: int, ql: int, qr: int, val: int = 1):
        if ql <= l and r <= qr:
            self._apply(node, l, r, val)
            return

        self._push(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)

        self.tree_sum[node] = (self.tree_sum[2 * node] + self.tree_sum[2 * node + 1]) % self.MOD
        self.tree_sq[node] = (self.tree_sq[2 * node] + self.tree_sq[2 * node + 1]) % self.MOD


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 1_000_000_007
        st = SegmentTree(n)
        last_pos = {}
        total_ans = 0

        for i, val in enumerate(nums):
            prev = last_pos.get(val, -1)
            st.update(1, 0, n - 1, prev + 1, i, 1)
            last_pos[val] = i
            total_ans = (total_ans + st.tree_sq[1]) % MOD

        return total_ans