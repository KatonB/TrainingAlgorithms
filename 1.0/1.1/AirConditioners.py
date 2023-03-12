def main():
    troom, tcond = map(int, input().split())
    mode = input()

    if (mode == 'heat' and tcond > troom) or (mode == 'freeze' and tcond<troom) or (mode == 'auto'):
        troom = tcond

    print(troom)

main()