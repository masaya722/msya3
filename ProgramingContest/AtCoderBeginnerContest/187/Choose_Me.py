N = int(input())
S = []
aoki = 0
takahashi = 0
for _ in range(N):
    a,b = map(int,input().split())
    aoki+=a
    S.append(a*2+b)
S.sort(reverse=True)
count = 0
while takahashi<=aoki:
    takahashi+=S[count]
    count+=1
print(count)