n,k = map(int,input().split())
n-=1
dp = [0]*(n+1)
dp[0] = 1
j=2
y=1
if n>0:
    dp[1] = 1

for i in range(2, n+1):
    if j<=k:
        for x in range(0,j):
            dp[i] += dp[x]
        j += 1
    elif j>k:
        for x in range(y, k+y):
            dp[i] += dp[x]
        y+=1


print(dp[n])