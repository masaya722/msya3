N = int(input())

M = []
for _ in range(0, N):
    S = input()
    S = list(S)
    M.append(S)

for i in range(N - 2, -1, -1):
    for j in range(1, N * 2 - 1):
        if M[i][j] == "#":
            if M[i + 1][j - 1] == "X":
                M[i][j] = "X"
            if M[i + 1][j] == "X":
                M[i][j] = "X"
            if M[i + 1][j + 1] == "X":
                M[i][j] = "X"
for i in range(0, N):
    M[i] = "".join(M[i])
    print(M[i])
