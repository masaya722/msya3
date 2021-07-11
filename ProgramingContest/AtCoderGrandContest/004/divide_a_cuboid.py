edges = list(map(int, input().split()))
edges.sort()
a =  edges[0]
b = edges[1]
c = edges[2]
if c%2 ==0:
    print(0)
else:
    print(a*b)
