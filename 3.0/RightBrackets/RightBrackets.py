string = input()
stack = []
openbr = ['(', '{', '[']
closebr = [')', '}', ']']
check = 0

for sym in string:
    if sym in openbr:
        stack.append(sym)
    elif sym in closebr:
        if len(stack) != 0 and openbr.index(stack.pop()) == closebr.index(sym):
            continue
        else:
            print('no')
            check = 1
            break

if len(stack) == 0 and check == 0:
    print('yes')
elif len(stack) != 0 and check == 0:
    print('no')