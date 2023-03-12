stack = []

while True:
    command = input()
    if command == 'exit':
        print('bye')
        break
    elif command == 'pop':
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
    elif command == 'size':
        print(len(stack))
    elif command == 'clear':
        while len(stack) != 0:
            stack.pop()
        print('ok')
    else:
        command, n = command.split()
        n = int(n)
        stack.append(n)
        print('ok')