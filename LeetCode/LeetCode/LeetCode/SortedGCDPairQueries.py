from math import gcd

class Solution:
    def gcdValues(self, nums, queries):
        m = max(nums)

        freq = [0] * (m + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (m + 1)
        for g in range(1, m + 1):
            for k in range(g, m + 1, g):
                cnt[g] += freq[k]

        exact = [0] * (m + 1)
        for g in range(m, 0, -1):
            c = cnt[g]
            exact[g] = c * (c - 1) // 2
            for k in range(2 * g, m + 1, g):
                exact[g] -= exact[k]

        prefix = []
        values = []
        total = 0
        for g in range(1, m + 1):
            if exact[g]:
                total += exact[g]
                values.append(g)
                prefix.append(total)

        import bisect
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix, q)
            ans.append(values[idx])

        return ans
