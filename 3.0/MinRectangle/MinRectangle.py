n = int(input())
x = [] * (n)
y = [] * (n)
ans = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

ans.append(min(x))
ans.append(min(y))
ans.append(max(x))
ans.append(max(y))

print(' '.join(str(elem) for elem in ans)) 