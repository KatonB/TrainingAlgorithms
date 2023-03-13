queue = []

while True:
    command = input()
    if command == 'exit':
        print('bye')
        break
    elif command == 'pop':
        if len(queue) == 0:
            print('error')
        else:
            print(queue.pop(0))
    elif command == 'front':
        if len(queue) == 0:
            print('error')
        else:
            print(queue[0])
    elif command == 'size':
        print(len(queue))
    elif command == 'clear':
        while len(queue) != 0:
            queue.pop(0)
        print('ok')
    else:
        command, n = command.split()
        n = int(n)
        queue.append(n)
        print('ok')