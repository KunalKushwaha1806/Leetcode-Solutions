class Solution:
    def comb(self, n: int, r: int, lim: int) -> int:
        r = min(r, n - r)
        ans = 1

        for i in range(1, r + 1):
            ans = ans * (n - r + i) // i
            if ans > lim:
                return lim + 1

        return ans

    def calc(self, cnt, rem, lim):
        ans = 1

        for x in cnt:
            if x == 0:
                continue

            ans *= self.comb(rem, x, lim)
            if ans > lim:
                return lim + 1

            rem -= x

        return ans

    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        n = len(s)
        m = n // 2
        ans = [' '] * n

        for i in range(26):
            if cnt[i] & 1:
                ans[m] = chr(ord('a') + i)

            cnt[i] //= 2

        if self.calc(cnt, m, k) < k:
            return ""

        for i in range(m):
            for c in range(26):
                if cnt[c] == 0:
                    continue

                cnt[c] -= 1
                cur = self.calc(cnt, m - i - 1, k)

                if cur >= k:
                    ans[i] = chr(ord('a') + c)
                    break

                k -= cur
                cnt[c] += 1

        for i in range(m):
            ans[n - 1 - i] = ans[i]

        return "".join(ans)