class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0

        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            ans += 1

        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]

            ans += 1 if dp[i][i + 1] else 0

        for length in range(3, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                ans += 1 if dp[i][j] else 0

        return ans

sol = Solution()

print(sol.countSubstrings("aaa"))