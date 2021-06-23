N = int(input())
S = list(input())
Q = int(input())
flag = False
for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if flag:
            a = (a+N)%(2*N)
            b = (b+N)%(2*N)
        S[a-1],S[b-1] = S[b-1],S[a-1]

    if t == 2:
        flag = not flag
if flag:
    S[0:N],S[N:] = S[N:],S[0:N]
print("".join(S))
