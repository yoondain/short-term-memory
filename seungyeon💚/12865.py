import sys

N, K = map(int, sys.stdin.readline().split())
bag = []

for _ in range(N):
    bag.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    w, v = bag[i][0], bag[i][1]
    if w <= K:
        dp[i+1][w] = max(dp[i+1][w], v)

    for j in range(1, K+1):
        if dp[i][j] != 0 and j+w <= K:
            dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j]+v)
        if dp[i][j] != 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
print(max(dp[N]))
