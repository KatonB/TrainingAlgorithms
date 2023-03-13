n = int(input())
dict = {}
wagons = []
for i in range(n):
    string = list(map(str, input().split()))
    if len(string)==3:
        command, count, type = string[0], int(string[1]), string[2]
    elif len(string)==2:
        command = string[0]
        if command == 'get':
            type = string[1]
        else:
            count = int(string[1])

    if command == 'add':
        wagons.append((count, type))
        if type in dict:
            dict[type]+= count
        else:
            dict[type]=0
            dict[type]+=count
    if command == 'get':
        if type in dict:
            print(dict[type])
        else:
            print(0)
    if command == 'delete':
        while count!=0:
            a, b = wagons.pop()
            if count > int(a):
                dict[b]-=a
                count -=a
            else:
                dict[b]-=count
                a-=count
                wagons.append((a,b))
                count=0