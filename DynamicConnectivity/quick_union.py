# Quick Union Algorithm
# The root of q becomes root of p

import time

class quickUnion:

    def __init__(self):
        self.mylist = []

    def initiate(self, N):
        self.mylist = [x for x in range(N)]
        print (self.mylist)

    def root(self,p):
        while self.mylist[p] != p:
            p = self.mylist[p]
        return p

    def connected(self, p, q):
        print (self.root(p))
        print (self.root(q))
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        start = time.time()
        self.mylist[i] = j
        print(self.mylist)
        end = time.time()
        print(end - start)


myArray = quickUnion()
myArray.initiate(100)

while quit != '0':
    p = int(input("Enter p:"))
    q = int(input("Enter q:"))

    print(myArray.connected(p,q))
    myArray.union(p, q)
    print(myArray.connected(p,q))

    quit = input("Enter 0 to exit 1 to continue")


