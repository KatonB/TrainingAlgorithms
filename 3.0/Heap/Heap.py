class Heap:
    def __init__(self):
        self.heap = []
        self.max = None
        self.ind = None

    def insert(self, item):
        self.heap.append(item)
        if len(self.heap) == 1 or item > self.max:
            self.max = item
            self.ind = len(self.heap)-1
        #print(self.heap)

    def extract(self):
        removed = self.heap[self.ind]
        l = len(self.heap)
        left = self.ind - 1
        self.max = None
        if l > 1:
            for i in range(self.ind, l-1):
                self.heap[i] = self.heap[i+1]
                if self.max == None or self.heap[i] > self.max:
                    self.max = self.heap[i]
                    self.ind = i
            for j in range(left, -1, -1):
                if (self.max == None or self.heap[j] > self.max) and j >= 0:
                    self.max = self.heap[j]
                    self.ind = j
        self.heap.pop()
        print(removed)


N = int(input())
h = Heap()

for i in range(N):
    string = list(map(int, input().split()))
    if len(string) == 1:
        h.extract()
    else:
        h.insert(string[1])