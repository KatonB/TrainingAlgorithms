NumOfSticks = int(input())
SticksNumbers = list(map(int, input().split()))
NumOfCollectors = int(input())
p = list(map(int, input().split()))

MaxNumStick = max(SticksNumbers)
MinNumStick = min(SticksNumbers)
SticksNumbersWD = sorted(list(set(SticksNumbers)))
NoDupl = len(SticksNumbersWD)
print(SticksNumbersWD)
#SticksNumbers = SticksNumbers.sort()
for i in range(NumOfCollectors):
    count = 0
    if p[i] < MinNumStick:
        print(0)
    elif p[i] > MaxNumStick:
        print(NoDupl)
    else:
        # syms = []
        # for j in range(len(SticksNumbersWD)):
        #     if SticksNumbersWD[j] < p[i] and SticksNumbersWD[j] not in syms:
        #         syms.append(SticksNumbersWD[j])
        #         count += 1
        # print(count)
        left, right = 0, NoDupl - 1
        while left <= right:
            mid = (left + right) // 2
            #print(mid)
            if SticksNumbersWD[mid] < p[i]:
                left = mid + 1
            else:
                right = mid - 1
        count = left
        print(count)


