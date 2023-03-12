a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print('NO SOLUTION')
elif c == 0:
    if b != 0 and a == 0:
        print('NO SOLUTION')
    elif b == 0 and a == 0:
        print('MANY SOLUTIONS')
    elif (b != 0 or b == 0) and a != 0:
        x = -b / a
        if x.is_integer():
            print(int(x))
        else:
            print('NO SOLUTION')
else:
    if a != 0:
        x = (c ** 2 - b) / a
        if x.is_integer():
            print(int(x))
        else:
            print('NO SOLUTION')
    else:
        if b == c**2:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
