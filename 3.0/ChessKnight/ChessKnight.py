n, m = map(int, input().split())

if m == 0:
    print(0)
else:
    dp = [[0] * (m) for i in range(n)]
    if n>1 and m>2:
        dp[1][2] = 1
    if n>2 and m>1:
        dp[2][1] = 1

    for i in range(2,n):
        for j in range(2,m):
                dp[i][j] = dp[i-2][j-1]+dp[i-1][j-2]

    # for i in range(0,n):
    #     print(dp[i])
    dp[0][0] = 1
    print(dp[n-1][m-1])