n = int(input())
h = []

#Просеивание вверх
def insert(h, x):
    h.append(x)
    pos = len(h)-1
    while pos>0 and h[pos] > h[(pos-1)//2]:
        h[pos], h[(pos-1)//2] = h[(pos-1)//2], h[pos]
        pos = (pos-1)//2
    #print(h)

#Просеиваниевниз
def extract(h):
    ans = h[0]
    h[0] = h[-1]
    pos = 0
    while pos*2 + 1 < len(h)-1:
        nextpos = pos*2+1
        if h[nextpos] < h[nextpos+1]:
            nextpos += 1
        if h[pos] < h[nextpos]:
            h[pos], h[nextpos] = h[nextpos], h[pos]
            pos = nextpos
        else:
            break
    h.pop()
    return ans



for i in range(n):
    string = list(map(int, input().split()))
    if len(string) == 1:
        print(extract(h))
    else:
        insert(h, string[1])