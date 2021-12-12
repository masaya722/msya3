from bisect import bisect_right

N,M = map(int,input().split())
cities = []
years = [[]for _ in range(N)]
for i in range(M):
    p,y = map(int,input().split())
    p -=1
    years[p].append(y)
    cities.append([p,y])

for i in range(N):
    years[i].sort()

for p,y in cities:
    idx = bisect_right(years[p],y)
    if p+1 <10**5:
        num1 = str(p+1)
        while len(num1)<6:
            num1 = "0"+num1
    else:
        num1 = str(p+1)
    if idx <10**5:
        num2 = str(idx)
        while len(num2)<6:
            num2 = "0"+num2
    else:
        num2 = str(idx)
    print(num1+num2)
    