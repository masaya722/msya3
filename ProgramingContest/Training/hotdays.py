D, N = map(int, input().split())
T = []
for _ in range(D):
    T.append(int(input()))
A = []
B = []
C = []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

score = []
for _ in range(D):
    score.append([-1]*101)
for i in range(N):
    if A[i] <= T[0] <= B[i]:
        score[0][C[i]] = 0
for i in range(1,D):
    for j in range(N):
        if A[j] <= T[i] <= B[j]:
            for k in range(101):
                if score[i-1][k] >= 0:
                    score[i][C[j]] = max(score[i][C[j]], score[i-1]
                                      [k] + abs(k-C[j]))

print(max(score[D-1]))