class Union_Find():
    rank = []
    parents = []
    size = []
    def __init__(self,n) -> None:
        for i in range(n):
            self.parents.append(i)
            self.rank.append(0)
            self.size.append(1)
    def find(self,x):
        if self.parents[x] ==x:
            return x
        else:
            return self.find(self.parents[x])
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x ==y:
            return
        if self.rank[y] >self.rank[x]:
            self.parents[x] = y
            self.size[y] +=self.size[x]
        else:
            if self.rank[x] ==self.rank[y]:
                self.rank[x]+=1
            self.parents[y] = x
            self.size[x]+=self.size[y]
    def same(self,x,y):
        return self.find(x) == self.find(y)