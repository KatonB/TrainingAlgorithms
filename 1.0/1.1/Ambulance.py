K1, M, K2, P2, N2 = map(int, input().split())

for i in range(1, 10 ** 6):
    y = K2 - (M * (P2 - 1) + N2 - 1) * i
    print(y)
    if 0 <= y <= i:
        x = i
        print(x)
        break

for i in range(10 ** 6):
    if i * M * x + 1 <= K1 <= (i + 1) * M * x:
        P1 = i + 1
        break

for i in range(x):
    N1 = (K1 - M * (P1 - 1) * x - i)/x
    if N1.is_integer():
        N1 = N1 + 1
        break

print(P1, ' ', int(N1))