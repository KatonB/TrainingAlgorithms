File = open('input.txt')
count = 0
for line in File:
    if count == 0:
        k = int(line.rstrip())
        count += 1
    elif count == 1:
        string = line.rstrip()
    else:
        break
File.close()

maxdist = 0
maxsym = ''

for i in range(0, len(string)):
    currsym = string[i]
    dist = 0
    for j in range(i, len(string)):
        if string[j] == currsym:
            dist += i + j - 1
            if dist > k:
                dist -= i + j - 1

    if dist >= maxdist:
        dist = maxdist
        maxsym = currsym

print(maxdist, maxsym)