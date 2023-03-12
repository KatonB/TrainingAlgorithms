n, m = map(int, input().split())
matrix = []
infinity = 99999
dp = [[infinity] * (m+1) for i in range(n+1)]

for i in range(n):
    row = list(map(int, input().split()))
    row.insert(0, infinity)  # добавление нулевого элемента в начало ряда
    matrix.append(row)
matrix.insert(0, [infinity] * (m + 1))
#print(matrix)

dp[1][1] = matrix[1][1]

for i in range(1, n+1):
    for j in range(1, m+1):
        if (i,j) != (1,1):
            dp[i][j] = min(dp[i-1][j]+matrix[i][j], dp[i][j-1] + matrix[i][j])


#print(dp)
print(dp[n][m])
