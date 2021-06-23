from collections import defaultdict as dd

n,m = map(int,input().split())

dict = dd(list)
for i in range(m):
    x,y = map(int,input().split())
    dict[x].append(y)

s = set()
s.add(n)
for d in dict:
    addList = list()
    for y in dict.values():
        if (y-1) in s or (y+1) in s:
            addList.append(y)
    for y in dict.values():
        s.remove(y)
    for y in addList:
        s.add(y)

print(len(s))

