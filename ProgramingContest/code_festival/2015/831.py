N,T = map(int,input().split())

A = []
B = []
diff = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    diff.append(a-b)

diff.sort(reverse=True)
total = sum(A)
lack = total -T

if lack<=0:
    print(0)
    exit()

cp = 0
count = 0
for d in diff:
    cp+=d
    count +=1
    if cp>= lack:
        print(count)
        exit()

print(-1)

