n = int(input())

dp = [0]*(n+1)
dp[0] = 1
if n>0:
    dp[1] = 2
if n>1:
    dp[2] = 4

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

print(dp[n])