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

N,M = map(int,input().split())
graph = [[]for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    if a<b:
        graph[a-1].append(b-1)
    else:
        graph[b-1].append(a-1)

uf = Union_Find(N)
ans = []
cnt = 0
for i in range(N-1,-1,-1):
    ans.append(cnt)
    cnt+=1
    if graph[i] != []:
        for j in graph[i]:
            if uf.same(i,j):
                continue
            uf.union(i,j)
            cnt-=1
ans.reverse()
for a in ans:
    print(a)