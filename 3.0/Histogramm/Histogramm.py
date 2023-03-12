def FillDict(string):
    dict = {}
    for sym in string:
        if sym != ' ':
            if sym not in dict:
                dict[sym] = 0
            dict[sym] += 1
    return dict


strings = ''
File = open('input.txt')
for line in File:
    line = line.rstrip()
    strings += line
File.close()

dictionary = FillDict(strings)
dictsort = sorted(dictionary.keys())
maxindict = max(dictionary.values())

for i in range(maxindict, 0, -1):
    for keys in dictsort:
        currvalueforkey = dictionary[keys]
        if currvalueforkey == i:
            print('#', end='')
            dictionary[keys] -= 1
        else:
            print(' ', end='')
    print()

for sym in dictsort:
    print(sym, end='')