N = int(input())
S = []
for i in range(N):
    a,b = map(int,input().split())
    S.append((b,a))

S.sort()

total = 0
for s in S:
    b,a = s
    total+=a
    if total >b:
        print("No")
        exit()
print("Yes")

