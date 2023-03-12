n = int(input())

A, B, C, dp = [0]*(n+3), [0]*(n+3), [0]*(n+3), [0]*(n+3)

for i in range(0,n+3):
    if i == 0 or i == 1 or i ==2:
        A[i], B[i], C[i] = 99999, 99999, 99999
    else:
        A[i], B[i], C[i] = map(int, input().split())

dp[0], dp[1], dp[2] = 0,0,0

for i in range(3,n+3):
    dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i-1], dp[i-3]+C[i-2])
    #print(dp[i-1]+A[i], dp[i-2]+B[i-1], dp[i-3]+C[i-2])

print(dp[n+2])