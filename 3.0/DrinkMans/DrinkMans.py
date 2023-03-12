First = list(map(int, input().split()))
Second = list(map(int, input().split()))
Count = 0

while len(First)!= 0 and len(Second)!=0 and Count != 10**6:
    Count += 1
    a = First.pop(0)
    b = Second.pop(0)
    if (a == 0 and b ==9) or (a > b and (a!=9 or b!=0)):
        First.append(a)
        First.append(b)
    if (b == 0 and a == 9) or (b > a and (b!=9 or a!=0)):
        Second.append(a)
        Second.append(b)

if len(First) == 0:
    print('second', Count)
else:
    print('first', Count)