N = int(input())
a = list(map(int, input().split()))
Stack = []
Answer = [0]*N

for i in range(N):
    if len(Stack) == 0:
        Stack.append([a[i], i])
    else:
        while len(Stack)!=0 and Stack[-1][0] > a[i]:
            b = Stack.pop()
            Answer[b[1]] = i
        Stack.append([a[i], i])

while len(Stack) != 0:
    b = Stack.pop()
    Answer[b[1]] = -1

print(*Answer)