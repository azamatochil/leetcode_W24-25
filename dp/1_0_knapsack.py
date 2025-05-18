class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)

        dp = [[0 for x in range(W + 1)]
        for x in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for c in range(1, W + 1):
                if wt[i] <= c:
                    dp[i][c] = max(val[i] + dp[i + 1][c - wt[i]], dp[i + 1][c])
                else:
                    dp[i][c] = dp[i + 1][c]
        return dp[0][W]


# {
# Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends