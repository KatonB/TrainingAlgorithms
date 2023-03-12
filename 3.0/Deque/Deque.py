stack = []

while True:
    command = input()
    if command == 'exit':
        print('bye')
        break
    elif command == 'pop_front':
        if len(stack) == 0:
            print('error')
        else:
            print(stack.pop(0))
    elif command == 'pop_back':
        if len(stack) == 0:
            print('error')
        else:
            print(stack.pop())
    elif command == 'back':
        if len(stack) == 0:
            print('error')
        else:
            a = stack.pop()
            stack.append(a)
            print(a)
    elif command == 'front':
        if len(stack) == 0:
            print('error')
        else:
            print(stack[0])
    elif command == 'size':
        print(len(stack))
    elif command == 'clear':
        while len(stack) != 0:
            stack.pop()
        print('ok')
    else:
        command, n = command.split()
        n = int(n)
        if command == 'push_front' and len(stack)!=0:
            a = len(stack)
            for i in range(a, 0, -1):
                if i == len(stack):
                    stack.append(0)
                stack[i] = stack[i-1]
            stack[0] = n
        else:
            stack.append(n)
        print('ok')