N = int(input())
S = input()

min_turn = 300000
sum_W = [0]
for i in range(0, N):

    if S[i] == 'W':
        sum_W.append(sum_W[i] + 1)
    else:
        sum_W.append(sum_W[i] + 0)

turn = []
for i in range(0, N):
    w = sum_W[i]
    e = N - (i+1) - (sum_W[N] - sum_W[i + 1])
    turn.append(w+e)


print(min(turn))
