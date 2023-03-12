def main():
    n=4
    code = '495'
    telnumbs = []
    for i in range(n):
        inp = input()
        inp = inp.replace("-", "").replace("(", "").replace(")", "").replace('+', '')
        if len(inp) == 11:
            inp = inp[1:]
        if len(inp) == 7:
            inp = code + inp
        if i!=0 and inp == telnumbs[0]:
            print('YES')
        elif i!=0:
            print('NO')
        telnumbs.append(inp)
        #print(telnumbs[i])
main()