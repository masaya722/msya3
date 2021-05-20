import itertools

N = int(input())
K = int(input())
card = []
for i in range(N):
    card.append(input())

ans = []
for arr in itertools.permutations(card, K):
    s = ''.join(arr)
    ans.append(s)

print(len(set(ans)))