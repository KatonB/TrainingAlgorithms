n, m = map(int, input().split())
matrix = []
infinity = -1
dp = [[infinity] * (m+1) for i in range(n+1)]
way = []
for i in range(n):
    row = list(map(int, input().split()))
    row.insert(0, infinity)  # добавление нулевого элемента в начало ряда
    matrix.append(row)
matrix.insert(0, [infinity] * (m + 1))
#print(matrix)

if (n,m) == (0,0):
    print(0)
elif (n,m) == (1,0):
    print(matrix[1][1])
elif (n,m) == (0,1):
    row = int(input())
    print(row)
else:
    dp[1][1] = matrix[1][1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i,j) != (1,1):
                dp[i][j] = max(dp[i-1][j]+matrix[i][j], dp[i][j-1] + matrix[i][j])

    # for i in range(n+1):
    #     print(dp[i])
    print(dp[n][m])

    i,j = n, m
    for k in range(n+m+2, 0, -1):
            if (i,j) == (1,1):
                break
            if dp[i-1][j] > dp[i][j-1]:
                #print(dp[i-1][j])
                way.append('D')
                i-=1
            elif dp[i-1][j] <= dp[i][j-1]:
                #print(dp[i][j-1])
                way.append('R')
                j-=1

    way.reverse()
    print(' '.join(way))
