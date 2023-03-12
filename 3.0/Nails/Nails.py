n = int(input())
cd = list(map(int, input().split()))
dp = [0]*(n+1)
cd.sort()

if n == 2:
    print(cd[0] + cd[1])
else:
    dp[0] = abs(cd[1] - cd[0])
    dp[1] = abs(cd[2] - cd[0])

    for i in range(2, n-1):
        dp[i] = min(dp[i-1], dp[i-2])+abs(cd[i]-cd[i+1])

    print(dp[n-2])