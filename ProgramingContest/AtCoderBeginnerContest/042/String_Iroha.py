S= []
N,L = map(int,input().split())
for _ in range(N):
    S.append(input())
S.sort()
print("".join(S))