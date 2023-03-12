N = int(input())
Wagons = list(map(int, input().split()))
Stack = []
SortW = []

for wag in Wagons:
    if len(Stack) == 0:
        Stack.append(wag)
    else:
        a = Stack.pop()
        if wag < a:
            Stack.append(a)
            Stack.append(wag)
        else:
            Stack.append(a)
            while len(Stack) != 0:
                a = Stack.pop()
                if a < wag:
                    SortW.append(a)
                else:
                    Stack.append(a)
                    break
            Stack.append(wag)

while len(Stack) != 0:
    SortW.append(Stack.pop())

if SortW == sorted(Wagons):
    print('YES')
else:
    print('NO')