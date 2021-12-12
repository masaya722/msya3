class UnionFind():
    def __init__ (self,n):
        self.parents = []
        self.rank  = []
        for i in range(n):
            self.parents.append(i)
            self.rank.append(0)
    def find(self,x):
        if self.parents[x] ==x:
            return x
        else:
            return self.find(self.parents[x])
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x ==y:
            return
        if self.rank[x]<self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x]+=1
    def same(self,x,y):
        return self.find(x) ==self.find(y)



N,Q =map(int,input().split())
uf = UnionFind(N)
for i in range(Q):
    p,a,b = map(int,input().split())
    a -=1
    b -=1
    if p ==0:
        uf.unite(a,b)
    else:
        if uf.same(a,b):
            print("Yes")
        else:
            print("No")

    

