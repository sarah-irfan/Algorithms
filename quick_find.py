# Quick Find Algorithm

import time

class quickFind:
    def __init__(self):
        self.mylist = []

    def initiate(self, N):
        self.mylist = [x for x in range(N)]
        print (self.mylist)

    def connected(self, p, q):
        return self.mylist[p] == self.mylist[q]

    def union(self, p, q):
        pid = self.mylist[p]
        qid = self.mylist[q]
        start = time.time()
        for x in range(len(self.mylist)):
            # print (x)
            if self.mylist[x] == pid:
                self.mylist[x] = qid
        print (self.mylist)    
        end = time.time()
        print(end - start)        


mm = quickFind()
mm.initiate(100)

while quit != '0':
    p = int(input("Enter p:"))
    q = int(input("Enter q:"))

    print(mm.connected(p, q))
    mm.union(p, q)
    print(mm.connected(p, q))

    quit = input("Enter 0 to exit 1 to continue")
