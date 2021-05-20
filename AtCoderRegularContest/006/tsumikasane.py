N = int(input())
W = [int(input()) for _ in range(N)]

top = []

for i in range(N):
    if i == 0:
        top.append(W[i])
    else:
        for j in range(len(top)):
            if top[j] >= W[i]:
                top[j] = W[i]
                break
        else:
            top.append(W[i])

print(len(top))
