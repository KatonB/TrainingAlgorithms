string = input().split()
stack = []

for sym in string:
    if sym == '+' and len(stack) > 1:
        stack.append(stack.pop() + stack.pop())
    elif sym == '*' and len(stack) > 1:
        stack.append(stack.pop() * stack.pop())
    elif sym == '-' and len(stack) > 1:
        a = stack.pop()
        stack.append(stack.pop() - a)
    else:
        stack.append(int(sym))

print(stack.pop())