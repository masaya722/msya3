b = list(input().split())
N = int(input())
S = []
for i in range(N):
    a = input()
    correct =[]
    for j in range(len(a)):
        c = b.index(a[j])
        correct.append(str(c))
    s = int(''.join(correct))
    S.append((s,a))

S.sort()
for i,j in S:
    print(j)