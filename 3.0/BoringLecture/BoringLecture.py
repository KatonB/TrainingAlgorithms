string = list(input())
d = {}
n = len(string)
for i in range(n):
    if i==0 or i==n-1:
        count = n
    else:
        count = n - i + i*n - i** 2

    if string[i] in d:
        d[string[i]]+=count
    else:
        d[string[i]] = count

sorted_keys = sorted(d.keys())
for key in sorted_keys:
    print(key + ': ' + str(d[key]))

